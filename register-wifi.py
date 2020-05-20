#!/usr/bin/env python3

import os
import sys

def Run_Windows():
    file = open("home-wifi.xml","w")

    file.write("<?xml version="1.0"?>\n")
    file.write("<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">\n")
    file.write("	<name>Nerd House_5G</name>\n")
    file.write("	<SSIDConfig>\n")
    file.write("		<SSID>\n")
    file.write("			<hex>4E65726420486F7573655F3547</hex>\n")
    file.write("			<name>Nerd House_5G</name>\n")
    file.write("		</SSID>\n")
    file.write("	</SSIDConfig>\n")
    file.write("	<connectionType>ESS</connectionType>\n")
    file.write("	<connectionMode>auto</connectionMode>\n")
    file.write("	<MSM>\n")
    file.write("		<security>\n")
    file.write("			<authEncryption>\n")
    file.write("				<authentication>WPA2PSK</authentication>\n")
    file.write("				<encryption>AES</encryption>\n")
    file.write("				<useOneX>false</useOneX>\n")
    file.write("			</authEncryption>\n")
    file.write("			<sharedKey>\n")
    file.write("				<keyType>passPhrase</keyType>\n")
    file.write("				<protected>false</protected>\n")
    file.write("				<keyMaterial>xxxxxxxx</keyMaterial>\n")
    file.write("			</sharedKey>\n")
    file.write("		</security>\n")
    file.write("	</MSM>\n")
    file.write("	<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">\n")
    file.write("		<enableRandomization>false</enableRandomization>\n")
    file.write("		<randomizationSeed>2955902897</randomizationSeed>\n")
    file.write("	</MacRandomization>\n")
    file.write("</WLANProfile>\n")

    file.close()

    cur_path = os.getcwd()
    os.system('powershell.exe netsh wlan add profile filename="' + cur_path + '\home-wifi.xml"')
    os.remove("home-wifi.xml")


def Run_MacOS():
    file = open("home-wifi.sh","w")

    file.write("#!/bin/bash\n\nnetworksetup -setairportnetwork en0 Nerd\ House_5G xxxxxxxx")

    file.close()

    cur_path = os.getcwd()
    os.system("chmod +x " + cur_path + "/home-wifi.sh")
    os.system(cur_path + "/home-wifi.sh")
    os.remove("home-wifi.sh")

def Run_Linux():
    file = open("home-wifi.sh","w")

    file.write("#!/bin/bash\n\niwconfig wlan0 essid Nerd\ House_5G key xxxxxxxx")

    file.close()

    cur_path = os.getcwd()
    os.system("chmod +x " + cur_path + "/home-wifi.sh")
    os.system(cur_path + "/home-wifi.sh")
    os.remove("home-wifi.sh")



cur_os = sys.platform()

if cur_os == "win32":
    Run_Windows()
elif cur_os == "darwin":
    Run_MacOS()
elif cur_os == "linux":
    Run_Linux()
else
    print("This is an unsupported platform")
