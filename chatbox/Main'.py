import nltk
import Responses
from nltk.tokenize import word_tokenize
import tkinter as tk
from tkinter import scrolledtext, Entry, Button, Label, Frame, END, Menu, messagebox
import datetime
import subprocess
import platform
import threading

# Download NLTK data
nltk.download('punkt_tab')
nltk.download('punkt')


class ChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.title("Network Troubleshooting Assistant")

        # Configure window appearance
        master.geometry("650x750")
        master.resizable(True, True)
        master.configure(bg='#f0f0f0')

        # Create menu bar
        self.create_menu()

        # Create main frames
        self.create_widgets()

        # Initial greeting
        self.display_system_message(f"Session started at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.display_bot_message("Hello! I'm your network troubleshooting assistant.")
        self.display_bot_message("You can ask about: no internet, slow WiFi, DNS errors, or router issues.")

    def create_menu(self):
        menubar = Menu(self.master)

        # File menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save Conversation", command=self.save_conversation)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_chat)
        menubar.add_cascade(label="File", menu=file_menu)

        # Tools menu
        tools_menu = Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Ping Test", command=lambda: self.run_network_test("ping"))
        tools_menu.add_command(label="Speed Test", command=lambda: self.run_network_test("speed"))
        tools_menu.add_command(label="Flush DNS", command=lambda: self.run_network_test("dns"))
        tools_menu.add_command(label="IP Config", command=lambda: self.run_network_test("ipconfig"))
        menubar.add_cascade(label="Network Tools", menu=tools_menu)

        # Help menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Help", command=self.show_help)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.master.config(menu=menubar)

    def create_widgets(self):
        # Chat frame
        self.chat_frame = Frame(self.master, bg='#f0f0f0')
        self.chat_display = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            width=80,
            height=25,
            state='disabled',
            font=('Segoe UI', 10),
            bg='white',
            fg='#333',
            padx=10,
            pady=10
        )
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Configure tags for colored messages
        self.chat_display.tag_config('user', foreground='#0066cc')
        self.chat_display.tag_config('bot', foreground='#009933')
        self.chat_display.tag_config('system', foreground='#666666')
        self.chat_display.tag_config('error', foreground='#cc0000')

        # Input frame
        self.input_frame = Frame(self.master, bg='#f0f0f0')
        self.user_input = Entry(
            self.input_frame,
            width=65,
            font=('Segoe UI', 10),
            bd=2,
            relief=tk.GROOVE
        )
        self.user_input.pack(side=tk.LEFT, padx=5, pady=5, ipady=3)
        self.user_input.bind("<Return>", self.send_message)

        # Send button
        self.send_button = Button(
            self.input_frame,
            text="Send",
            command=self.send_message,
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049',
            font=('Segoe UI', 10, 'bold'),
            padx=12
        )
        self.send_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Status indicator
        self.status_label = Label(
            self.input_frame,
            text="✓ Online",
            fg="green",
            bg='#f0f0f0',
            font=('Segoe UI', 9)
        )
        self.status_label.pack(side=tk.LEFT, padx=10)

        # Exit button
        self.exit_button = Button(
            self.input_frame,
            text="Exit",
            command=self.exit_chat,
            bg='#f44336',
            fg='white',
            activebackground='#d32f2f',
            font=('Segoe UI', 10),
            padx=12
        )
        self.exit_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # Pack frames
        self.chat_frame.pack(fill=tk.BOTH, expand=True)
        self.input_frame.pack(fill=tk.X, pady=(0, 10))

    def display_message(self, sender, message, msg_type='normal'):
        self.chat_display.config(state='normal')

        # Add timestamp
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(END, f"[{timestamp}] ", 'system')

        # Add sender tag
        if sender.lower() == "user":
            self.chat_display.insert(END, f"You: ", 'user')
        elif sender.lower() == "system":
            pass  # No sender prefix for system messages
        else:
            self.chat_display.insert(END, f"Bot: ", 'bot')

        # Add message with appropriate formatting
        self.chat_display.insert(END, f"{message}\n", msg_type)

        self.chat_display.config(state='disabled')
        self.chat_display.see(END)

    # Convenience methods for specific message types
    def display_user_message(self, message):
        self.display_message("user", message)

    def display_bot_message(self, message):
        self.display_message("bot", message)

    def display_system_message(self, message):
        self.display_message("system", message)

    def display_error_message(self, message):
        self.display_message("system", message, 'error')

    def send_message(self, event=None):
        user_input = self.user_input.get().strip()
        if not user_input:
            return

        self.display_user_message(user_input)
        self.user_input.delete(0, END)

        if user_input.lower() == "exit":
            self.exit_chat()
            return

        # Process the message in a separate thread to keep UI responsive
        threading.Thread(target=self.process_user_input, args=(user_input,), daemon=True).start()

    def process_user_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        response = self.get_best_response(tokens)
        self.display_bot_message(response)

    def get_best_response(self, tokens):
        # First check for exact multi-word matches
        for phrase, response in Responses.responses.items():
            if all(word in tokens for word in phrase):
                return response

        # Then check for partial matches
        for phrase, response in Responses.responses.items():
            if any(word in tokens for word in phrase):
                return response

        # Final fallback
        return ("I'm not sure I understand. Could you try rephrasing?\n"
                "Here are things I can help with:\n"
                "- No internet\n- Slow connection\n- WiFi issues\n- DNS errors")

    def save_conversation(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"chat_history_{timestamp}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(self.chat_display.get('1.0', END))
            self.display_system_message(f"Conversation saved to {filename}")
        except Exception as e:
            self.display_error_message(f"Error saving file: {str(e)}")

    def run_network_test(self, test_type):
        def run_command():
            try:
                self.display_system_message(f"Running {test_type} test...")

                if test_type == "ping":
                    target = "8.8.8.8"  # Google DNS
                    param = "-n" if platform.system().lower() == "windows" else "-c"
                    command = ["ping", param, "4", target]
                elif test_type == "dns":
                    if platform.system().lower() == "windows":
                        command = ["ipconfig", "/flushdns"]
                    else:
                        command = ["sudo", "systemd-resolve", "--flush-caches"]
                elif test_type == "ipconfig":
                    if platform.system().lower() == "windows":
                        command = ["ipconfig", "/all"]
                    else:
                        command = ["ifconfig"]
                else:  # speed test
                    self.display_bot_message("Speed test requires an internet connection...")
                    return

                result = subprocess.run(command, capture_output=True, text=True, timeout=15)

                if result.returncode == 0:
                    output = result.stdout.strip()
                    self.display_bot_message(f"{test_type.upper()} Results:\n{output[:500]}")  # Limit output length
                else:
                    self.display_error_message(f"{test_type} test failed:\n{result.stderr.strip()}")

            except Exception as e:
                self.display_error_message(f"Error running {test_type} test: {str(e)}")

        threading.Thread(target=run_command, daemon=True).start()

    def show_about(self):
        about_text = """Network Troubleshooting Assistant v1.1
Created for IT Support Portfolio

Features:
- Natural language processing
- Network diagnostics tools
- Conversation history logging
- Step-by-step troubleshooting guides"""
        messagebox.showinfo("About", about_text)

    def show_help(self):
        help_text = """How to use this assistant:
1. Describe your network issue (e.g., "no internet", "slow WiFi")
2. Follow the troubleshooting steps provided
3. Use the Network Tools menu for diagnostics

Common commands:
- Type 'exit' to end the session
- Ask about specific errors
- Request router recommendations"""
        messagebox.showinfo("Help", help_text)

    def exit_chat(self):
        self.display_system_message(f"Session ended at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.display_bot_message("Goodbye! Feel free to come back if you have more network issues.")
        self.master.after(1000, self.master.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()