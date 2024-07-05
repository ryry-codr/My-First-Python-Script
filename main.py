import time

server = input("Server Address: ")
time.sleep(2)

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

print("Thank You For Logging In " + username + "" )