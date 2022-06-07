# 70mai A500S Bootsound Toggle
This script will disable or enable the startup sound on the 70mai A500S dash cam.

### Instructions

**1) Install Python**<br>
Download and install [Python](https://www.python.org/downloads/). It's needed in order to run this script.

**2) Download the script**<br>
The latest version can be found [here](https://github.com/bauluk/70mai-A500S-Bootsound-Toggle/releases/) (click on "bootsound.py").

**3) Enable the Wi-Fi hotspot on the dash cam**<br>
You'll need to have the dash cam near your computer and powered on. The hotspot can be enabled in the settings on the device.

**4) Connect to it on your computer**<br>
You should now see the dash cam on your list of Wi-Fi networks. Enter the password that was presented to you, and connect to it.

**5) Run the script**<br>
Once successfully connected you can now [run the script](https://www.wikihow.com/Open-a-Python-File). It will prompt you with an option. Type a number choice, and press enter on your keyboard. Wait for the script to complete.

**6) Confirm the results**<br>
The sound should now be disabled, or enabled depending on what you chose. You can confirm this by powering off your dash cam and turning it back on.

<hr>

**Why did you make this?**

The bootsound on this particular model is especially loud, and the output is rough sounding. I couldn't find an official way to disable it.

**What does this script do on a technical level?**

A port scan of the device revealed a telnet server. Connecting to it as the username "root" with no password grants a shell. I then located the bootsound file and renamed it. That prevented the sound from playing again when the dash cam powered on. This script simply automates that process.

**What are the limitations?**

The script doesn't know whether or not you've ran it before. This is due to the lack of reliable output from the telnet protocol. However, this won't matter for the average user. If you're manually tinkering around on the telnet service, and rename or remove the file, the script won't be aware. Doing so can cause it to report invalid results.
