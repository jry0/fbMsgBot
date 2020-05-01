from fbchat import Client

# Get login credentials from file
fileLogin = open("C:/Users/JerryX/Desktop/fbChatLogin.txt", "r")
userEmail = str(fileLogin.readline())
userPwd = str(fileLogin.readline())
fileLogin.close()
print("Email: ", userEmail)
print("Password: ",userPwd)

# Attempt login
clientBarry = Client(userEmail, userPwd, max_tries = 1)
sessionBarry = clientBarry.getSession()
print(sessionBarry)


searchName = input("Input name to search: ")
searchedUserList = clientBarry.searchForUsers("Jerry Xing", limit = 5)

print("ID: ", searchedUserList[0].uid)


clientBarry.logout()