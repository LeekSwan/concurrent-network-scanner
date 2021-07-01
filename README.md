# Overview
This is a ping based concurrent network scanner. It utilizes asyncio to scan in parallel 


# How to run
 Download and the pindiscover.py and run in cmd.  
 Takes 3 arguments: subnet/mask, concurrency level, and timeout.  
 Eg input to scan hosts on subnet 192.168.0.0/24 5 at a time with a timeout of 2: "pingdiscover.py 192.168.0.0/24 --concurrent 5 --timeout 2"
 
# Notes
 Only import from 3rd party is aioping: https://github.com/stellarbit/aioping
 Install using pip install aioping
 The rest of the imports are built-in

