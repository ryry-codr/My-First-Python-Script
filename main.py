import time, os

server = input("Server Address: ")

print ("Connecting to server: " + server + "")
time.sleep(5)

print ("Connection Established!")
time.sleep(3)

print ("Welcome User")
time.sleep(1)

username = input("Username: ")
print ("Processing...")
time.sleep(2)

password = input("Password: ")
print ("Processing...")
time.sleep(2)

print("You are now connected to " + server + "")
time.sleep(1)
print("Thank You For Logging In " + username + "" )
time.sleep(1)
print("" + username + ", If you are not authorized to be connected, please disconnect now.")

time.sleep(1)
Disconnect = input("Would you like to disconnect? (Y/N): ")
if Disconnect == 'Y':
    os.system("cls")
    print("Disconnecting...")
    time.sleep(3)
    print("Disconnected")
    time.sleep(1)
    print("Exiting...")
    exit()
elif Disconnect == 'y':
    os.system("cls")
    print("Disconnecting...")
    time.sleep(3)
    print("Disconnected")
    time.sleep(1)
    print("Exiting...")
    exit()
elif Disconnect == 'N':
    print("Ok, now loading data on " + server + "")
    if server == "Ryan-Laptop":
        print("!WARNING! NON-AUTHORIZED CONNECTION, DISCONNECTING. !WARNING!")
        time.sleep(3)
        print("Crashed with code noauth")
        time.sleep(3)
        exit()
    else:
        print("Message from " + server + ": Yeah I can't really load anything because I'm not a real server, this is just a (not so) simple python program with 76 lines of code, so I'm just going to exit in 10 seconds.")
        time.sleep(10)
        print("Exiting...")
        exit() 
elif Disconnect == 'n':
    print("Ok, now loading data on " + server + "")
    if server == "Ryan-Laptop":
        print("!WARNING! NON-AUTHORIZED CONNECTION, DISCONNECTING. !WARNING!")
        time.sleep(3)
        print("Crashed with code noauth")
        time.sleep(3)
        exit()
    else:
        print("Message from " + server + ": Yeah I can't really load anything because I'm not a real server, this is just a (not so) simple python program with 76 lines of code, so I'm just going to exit in 10 seconds.")
        time.sleep(10)
        print("Exiting...")
        exit()
else:
    print("Crashed with code invalidinput")

    time.sleep(3)
    exit()
