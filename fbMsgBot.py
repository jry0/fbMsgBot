from fbchat import Client
from fbchat.models import *

#from getpass import getpass
# Get login credentials from file
fileLogin = open("C:/Users/JerryX/Desktop/fbChatLogin.txt", "r")
userEmail = str(fileLogin.readline())
userPwd =   str(fileLogin.readline())
fileLogin.close()
print("Email: ", userEmail)
print("Password: ",userPwd)

# Attempt login
clientBarry = Client(userEmail, userPwd, max_tries = 1)
print(clientBarry.getSession())

# Search for user
searchName = input("Input name to search: ")
searchedUserList = clientBarry.searchForUsers(searchName, limit = 5)


for searchedUser in searchedUserList:
    # Print User Info
    print("ID: ", searchedUser.uid)
    print("Photo: ", searchedUser.photo)
    print("Is Friend: ", searchedUser.is_friend)

    # Confirm User 
    if(input("Correct User? (Y/N): ").lower() == "y"):

        # Send an opener (image)
        clientBarry.sendLocalImage(
            "C:/Users/JerryX/Pictures/jazz.png", 
            message = Message(text="SALUTATIONS 👋"),
            thread_id = searchedUser.uid,
            thread_type= ThreadType.USER
        )

        # Send-message loop, send nothing to exit and logout
        while True:
            msg = input("Send message: ")
            if msg:
                clientBarry.send(
                    Message(text=msg),
                    thread_id=searchedUser.uid,
                    thread_type = ThreadType.USER
                )
            else:
                break
    break
# Logout
try:
    clientBarry.logout()
    print("User logged out.")
except:
    print("Error logging out.")