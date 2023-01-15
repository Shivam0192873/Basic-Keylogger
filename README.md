# Objective:
The purpose of this project is to understand how a programming of a software is done in
systematic manner and gain knowledge about software engineering and cybersecurity.
Awareness about the cybersecurity and understand the malicious cyber activities and about
the keyloggers which usually used as spyware


# What is a keylogger and this project about?
Keyloggers incorporate a wide array of cyber security issues and provide a practical
approach to understand topics such as attacker goals, varieties of malware and their
implementation, the role of malware in infecting and how stealth is archived in an infected
system. On the contrary, a lot of malicious software utilizes keyloggers in the attempt to
retrieve usernames and passwords for different websites.
Keyloggers are a genuine danger to clients and the clients' information, which is considered
exploitative movement.
This is a spyware application used to track the users which logs keystrokes. Using this
spyware, unlawful cybercrimes are being committed. In this keylogger project, wheneverSmtplib
the user types something through the keyboard, the keystrokes are captured and mailed to
the mail id of creator of the project without the knowledge of the user within the capture
limit set.


# Purpose:
The main objective of this project is to illustrate the requirements of the project Keylogger. And to
understand the ways the cybercrimes are being committed and understand is logically and how a
programming of a software takes place using simple and understandable approach of the program
using proper modular functions and modular programming.
Keystroke loggers are available in software and hardware form, and are used to capture and compilea
record of all typed keys. The information gathered from a keystroke logger is saved in the list created
as key and emailed to the creator of the project. Generic keystroke loggers typically record the
keystrokes associated with the keyboard typing. Our project keylogger has the following features;
1) Monitors Keystrokes
2) Sends mail to the project creator’s mail Id
3) Logs keystrokes including special keys
4) Software Engineering


# Modules used:
1) Smtplib: The module included in python defines an SMTP client session object that can beused to
send mail to any internet machine with an SMTP listener daemon
2) SSL: SSL stands for Secure Sockets Layer and is designed to create secure connection between client
and server. Secure means that connection is encrypted and therefore protected from eavesdropping. It
also allows to validate server identity.
3) Pynput: This library allows the users to control and monitor input devices. e.g.; pynput.mouse,
pynput.keyboard.

# Features:
Features of designed keylogger that are implemented and are going to be implemented in this project;
1) Keystroke Recording
2) Remote Monitoring
3) Invisible mode
4) Email reports


# Hardware requirements:
1) Operating system : Windows
2) RAM : 512MB (minimum requirement)
3) Hard Disk : 1GB working space (minimum requirement)


# Software requirements:
1) Languages : Python
2) Tools : PyCharm, Python 3.8.0 and above.
3) Technology : Advanced programming using Python


# How to run it?

1) Download the repo. 
2) Navigate to the downloaded folder. 
3) Open "code.py" and make changes (put your email id in the required fields).
4) Open command prompt/terminal and navigate to the keylogger directory that you have downloaded.
5) Type "python code.py" and the program will start capturing the keystrokes and will be send to the provided email id.


# How to convert PY to EXE?
1) Install pyinstaller useing: pip install pyinstaller
2) Covert PY to EXE using pynstaller: 

# If it's not working!

If the keystrokes are not being sent to your provided email id then make sure to turn on the "allow less secure apps" (maybe different for other than google accounts) settings in your account.

It is suggested to set up a dummy account for testing purpose.
