# Packet Manipulation via Scapy

This repository is a lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab we are going to learn how to use Scapy - a powerful interactive packet manipulation program, which can forge or decode packets of a wide number of protocols, send them on wire, capture them, match requests and replies, and much more.

---
## Objectives

1. Learn how to define your own protocol and generate a packet payload
2. Learn how to use Wireshark to filter packets and find your wanted information

This lab aims to learn how we use Scapy and Python to program a simple network protocol and observe the behavior of packet sending and receiving via Wireshark.

* Basic knowledge of Docker
* Linux networking
* Python with Scapy
* Wireshark

---
## Overview

![](https://i.imgur.com/7RFvA3l.png)

* Define our own proprietary protocol
* In this protocol, we will iteratively send to a server
    1. ID packet: your (ID + department + gender)
    2. Secret packet: a digit of the secret key
* The above procedure will repeat 14 times so that you will collect a 14-digit secret key
    * E.g., 41228904512480

![](https://i.imgur.com/276Z0iA.png)

### Packet Format

* ID Packet
    ![](https://i.imgur.com/37C6IJE.png)
* Secret Packet
    ![](https://i.imgur.com/Ci9fJa5.png)

---
## Installation

* **Docker (Docker CE)**
    * [Windows](https://docs.docker.com/docker-for-windows/)
    * [MacOS](https://docs.docker.com/docker-for-mac/)
    * [Ubuntu Linux](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
    * [Others](https://docs.docker.com/install/)
* **[Wireshark 2.6.3](https://www.wireshark.org/download.html)**
    * Windows ([32-bit](https://1.as.dl.wireshark.org/win32/Wireshark-win32-2.6.3.exe) / [64-bit](https://1.as.dl.wireshark.org/win64/Wireshark-win64-2.6.3.exe))
    * [MacOS](https://1.as.dl.wireshark.org/osx/Wireshark%202.6.3%20Intel%2064.dmg)
    * Ubuntu Linux
        ```bash
        $ sudo apt-get install -y wireshark
        ```
* Others
    * [PieTTy](https://drive.google.com/file/d/0BxKoW6fgUa0CSTJDMmlDNC1nUDg/view) (for Windows)

---
## Tasks

* **In lab assignement**
    1. Environment Setup
    2. Define protocol via Scapy
    3. Send packets
    4. Sniff packets
    5. Run sender and receiver
    6. Push your files to remote
* **Homework assignement**
    1. Load PCAP via Wireshark
    2. Filter the target packet
    3. Decode the secret key
    4. Report

### File Structure

```bash
Packet Manipulation/                # This is ./ in this repository
|--- docker/                        # Docker configuration
     |--- Dockerfile
     |--- main.sh                   # Scripts for running Docker
     |--- [Other files...]
|--- src/                           # Source code
     |--- data/                     # Input files
          |--- record.txt           # Example file for R/W
     |--- out/                      # Output files
     |--- scripts/                  # Networks configuration
          |--- main.sh              # Scripts for build namespace
          |--- [Other files...]
     |--- sender.py                 # Send packets
     |--- receiver.py               # Receive and sniff packets
     |--- Protocol.py               # Define your own protocol
     |--- decoder.py                # Decode the output file
|--- LICENSE
|--- README.md
```

---
## Contributor

* [David Lu](https://github.com/yungshenglu)

---
## License

[GNU GENERAL PUBLIC LICENSE Version 3](LICENSE)