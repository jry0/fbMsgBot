from fbchat import Client, log
from fbchat.models import Message, ThreadType
from scriptScraper import getBeeMovieScript


# Subclass of Client()
# Override __init__ and onMessage() method
# Add new webscrapping method getBeeMovieScript
cli = Client
class ResponseBot(Client):
    
    def __init__(self, userEmail, userPwd ):
        self.flagScriptTrigger = False
        super().__init__(userEmail, userPwd, max_tries = 1) # More research needed into init overloading for subclasses
                                                            # Error encountered when specifying parameter names (multiple instaces)
                                                            # No 'self' is passed thru to parent Client()

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # Reponse to incoming message
        if author_id != self.uid:
            
            # Exit Condition
            if message_object.text.lower() == "bye": 
                self.send(Message(text = "Goodbye 👋"), thread_id=thread_id, thread_type=thread_type)
                # Brute force logout, Client keeps trying to reconnect
                self.logout() 

            # returns weather data
            elif message_object.text.lower()[0:7] == "weather": 
                self.send(Message(text = message_object.text[8:]), thread_id=thread_id, thread_type=thread_type)
            
            # One time trigger
            elif self.flagScriptTrigger == False: 
                # Set flag
                self.flagScriptTrigger = True
                # Get bee script, split into lines, and print
                beeScript = getBeeMovieScript().splitlines() 
                for scriptLine in beeScript: 
                    self.send(Message(text=scriptLine), thread_id=thread_id, thread_type=thread_type)


# Get login credentials from file
fileLogin = open("C:/Users/JerryX/Desktop/fbChatLogin.txt", "r")
userEmail = str(fileLogin.readline())
userPwd =   str(fileLogin.readline())
fileLogin.close()
print("Email: ", userEmail)
print("Password: ",userPwd)

# Attempt login
clientBarry = ResponseBot(userEmail, userPwd) # instantiate of Client subclass
print(clientBarry.getSession())

# Search for user
searchName = input("Input name to search: ")
searchedUserList = clientBarry.searchForUsers(searchName, limit = 5)


for searchedUser in searchedUserList:
    # Print User Info
    print("Name: ", searchedUser.name)
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
# try:
#     clientBarry.logout()
#     print("User logged out.")
# except:
#     print("Error logging out.")