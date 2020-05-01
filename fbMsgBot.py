from fbchat import Client, log
from fbchat.models import *



# Subclass fbchat.Client and override required methods
class ResponseBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            if message_object.text.lower() == "bye":
                self.send(Message(text = "Goodbye 👋"), thread_id=thread_id, thread_type=thread_type)
                self.logout()
            else:
                self.send(Message(text="This is an automated response."), thread_id=thread_id, thread_type=thread_type)






# Get login credentials from file
fileLogin = open("C:/Users/JerryX/Desktop/fbChatLogin.txt", "r")
userEmail = str(fileLogin.readline())
userPwd =   str(fileLogin.readline())
fileLogin.close()
print("Email: ", userEmail)
print("Password: ",userPwd)

# Attempt login
clientBarry = ResponseBot(userEmail, userPwd, max_tries = 1) # instance of Client subclass
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

        # Listen for inbound? message
        clientBarry.listen()

        # # Send-message loop, send nothing to exit and logout
        # while True:
        #     msg = input("Send message: ")
        #     if msg:
        #         clientBarry.send(
        #             Message(text=msg),
        #             thread_id=searchedUser.uid,
        #             thread_type = ThreadType.USER
        #         )
        #     else:
        #         break

        break 
# Logout
try:
    clientBarry.logout()
    print("User logged out.")
except:
    print("Error logging out.")