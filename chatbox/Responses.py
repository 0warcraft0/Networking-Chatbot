responses = {
    # General greeting to start troubleshooting
    ("hi", "hello", "hey"): "Hello! I'm your network troubleshooting assistant. Are you having issues with your internet, Wi-Fi, or connectivity?",

    # No Internet Connection
    ("no", "internet"): "No internet? Let's fix it! 1) Check if your router's power light is on. 2) Restart your router by unplugging it for 30 seconds, then plugging it back in. 3) Ensure your device is connected to the Wi-Fi network. 4) If still no luck, try connecting directly to the router with an Ethernet cable. Does any of that help? If not, let me know what you see!",
    ("internet", "not", "working"): "Internet down? Here's what to try: 1) Verify your modem and router are powered on. 2) Reboot both by unplugging them for 30 seconds. 3) Check Wi-Fi signal strength or try a wired connection. 4) If it's still not working, contact your ISP to check for outages. Any progress? Tell me more!",
    ("can't", "connect"): "Can't connect to the internet? Try this: 1) Confirm your Wi-Fi is enabled and you're connected to the right network. 2) Restart your router and device. 3) Forget the Wi-Fi network on your device and reconnect with the correct password. 4) Check if other devices can connect. Still stuck? Let me know what's happening!",

    # Wifi Issues
    ("wifi", "isnt", "working"): "WiFi isn't working? Let's fix it: 1) Check you're in range of the router. 2) Restart your router and device. 3) Verify other devices can connect to the WiFi. 4) If none work, log into your router (try 192.168.1.1) to check settings. Any luck? Tell me what's happening!",
    ("wifi", "not", "working"): "WiFi trouble? Let's sort it out: 1) Ensure you're in range of the router. 2) Restart your router and device. 3) Check if other devices can connect to the WiFi. 4) If no devices work, log into your router (usually 192.168.1.1) and verify settings. Any change? Describe what's going on!",
    ("wifi", "dropping"): "WiFi keeps dropping? Here's what to do: 1) Move closer to the router to avoid interference. 2) Check for devices like microwaves or cordless phones that might disrupt the signal. 3) Restart your router. 4) Update your router's firmware via its admin page (check the manual for details). Still dropping? Tell me more!",
    ("no", "wifi"): "No WiFi signal? Try these steps: 1) Confirm your router is powered on and WiFi is enabled. 2) Check if the WiFi name (SSID) is visible on your device. 3) Restart your router and device. 4) If the SSID still doesn't show, your router may need a reset—check its manual. Any luck? Let me know!",
    ("slow", "wifi"): "Slow WiFi? Here's the plan: 1) Ensure you're close to the router. 2) Reduce connected devices (like smart TVs or phones). 3) Change your WiFi channel in the router settings to avoid interference (use 1, 6, or 11 for 2.4GHz). 4) Consider a WiFi extender if the signal is weak. Still slow? What's the status?",
    ("phone", "no", "wifi"): "Phone not getting WiFi? Try this: 1) Toggle WiFi off and on. 2) Forget the network and reconnect with the password. 3) Restart your phone and router. 4) Check if other devices connect to the WiFi. If not, it's likely the router. Any progress? Let me know what's up!",

    # Error specific responses
    ("dns_probe_finished_no_internet",): "For DNS_PROBE_FINISHED_NO_INTERNET: 1) Clear browser cache 2) Flush DNS (ipconfig/flushdns) 3) Change DNS to 8.8.8.8 4) Disable VPN/proxy",

    # Hardware suggestions
    ("recommend", "router"): "For better performance consider: 1) TP-Link Archer AX73 (best value) 2) ASUS RT-AX86U (gaming) 3) Netgear Orbi (mesh systems) 4) Check WiFi 6 support",

    # Slow Internet
    ("slow", "internet"): "Slow internet? Let's speed it up: 1) Run a speed test (try speedtest.net) to confirm. 2) Disconnect unused devices from your WiFi. 3) Move closer to your router or use a wired connection. 4) Restart your router. If it's still slow, your ISP might be throttling—contact them. How's it going now?",
    ("internet", "slow"): "Internet crawling? Try this: 1) Check how many devices are connected to your network. 2) Restart your router and modem. 3) If using WiFi, switch to the 5GHz band if available (check router settings). 4) Test with an Ethernet cable to rule out WiFi issues. Any improvement? Let me know!",

    # DNS Issues
    ("DNS", "error"): "DNS error? Let's fix it: 1) Restart your router and device. 2) Try switching to a public DNS like Google's (8.8.8.8 and 8.8.4.4) in your device's network settings. 3) Clear your DNS cache (on Windows, run 'ipconfig /flushdns' in Command Prompt). 4) Check if your ISP has DNS issues. Does that help? Tell me more!",
    ("can't", "load", "website"): "Websites not loading? It might be DNS: 1) Try a different website to confirm it's not site-specific. 2) Restart your router. 3) Switch to Google DNS (8.8.8.8) in your network settings. 4) Run 'ipconfig /flushdns' on Windows or restart your device. Still not working? What error do you see?",

    # IP Address Conflicts
    ("IP", "conflict"): "IP address conflict? Here's what to do: 1) Restart your router to assign new IP addresses. 2) On your device, release and renew the IP (on Windows, run 'ipconfig /release' then 'ipconfig /renew'). 3) Ensure your router's DHCP is enabled (check settings at 192.168.1.1). 4) If it persists, set a static IP outside the DHCP range. Fixed? Let me know!",
    ("network", "conflict"): "Network conflict issue? Try this: 1) Power cycle your router and devices. 2) Check for duplicate devices using the same IP (run 'arp -a' on Windows). 3) Renew your device's IP (Windows: 'ipconfig /release' then '/renew'). 4) Log into your router and confirm DHCP is active. Any change? What's happening?",

    # Router Issues
    ("router", "not", "working"): "Router acting up? Let's troubleshoot: 1) Check all cables are secure and lights are on. 2) Restart the router (unplug for 30 seconds). 3) Log into the router (try 192.168.1.1) and verify settings. 4) If no response, reset the router to factory settings (hold reset button for 10 seconds). Any luck? Tell me more!",
    ("no", "router"): "No router connection? Try these: 1) Ensure the router is powered on and lights are blinking. 2) Check cable connections (Ethernet or WAN). 3) Restart the router and modem. 4) If it's still not working, try a factory reset (check the manual for the reset button). Does it connect now? What do you see?",

    # Device-Specific Issues
    ("computer", "no", "internet"): "Computer can't connect? Here's what to do: 1) Confirm WiFi or Ethernet is enabled. 2) Restart your computer and router. 3) Run Windows Network Troubleshooter (Settings > Network > Troubleshoot). 4) Update network drivers (Device Manager > Network Adapters). Still no connection? Describe the error!",

    # General Network Troubleshooting
    ("network", "problem"): "Network issues? Let's diagnose: 1) Restart your modem, router, and device. 2) Check if it's WiFi or wired (try an Ethernet cable). 3) Run a ping test (Windows: 'ping 8.8.8.8' in Command Prompt). 4) If no response, contact your ISP. What's the situation now?",
    ("connection", "issues"): "Connection problems? Here's a plan: 1) Verify all cables are plugged in. 2) Restart your router and device. 3) Check signal strength if on WiFi. 4) Test with another device to isolate the issue. Still not connecting? Tell me what you're seeing!",

    # Fallback for unrecognized issues
    ("troubleshoot",): "Want to troubleshoot a network issue? Tell me more, like 'no WiFi,' 'slow internet,' or 'DNS error,' and I'll guide you through the steps!",
    ("network",): "Network trouble? Can you specify, like 'no internet,' 'WiFi dropping,' or 'slow connection'? I'll help you fix it step-by-step!"
}