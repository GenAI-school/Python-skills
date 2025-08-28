class chatbook:
    __bankbalance = 0
    def __init__(self):
        self.__name = "communication platform"
        chatbook.__bankbalance+=10000
        self.userName = ''
        self.password = ''
        self.loggedIn = False
        #self.menu()

    def menu(self):
        User_input = input(""""1.Press 1 to signup 2.Press 2 to Signin 3.Press 3 to write a post 4.Press 4 to message a friend 5.Press any other key to exit""")
        if User_input == '1':
            self.signup()
        elif User_input == '2':
            self.signin()
        elif User_input == '3':
            self.writepost()
        elif User_input == '4':
            self.messagefriend()
        else:
            print("Thank you for using chatbook")
    @staticmethod
    def get_bal():
        return chatbook.__bankbalance
    
    @staticmethod
    def set_bal(amount):
        chatbook.__bankbalance = amount



    def signup(self):
        self.userName = input("Enter your username : ")
        self.password = input("Enter your password : ")
        print(f"User {self.userName} signed up successfully")
        self.menu()

    def signin(self):
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        if username == self.userName and password == self.password:
            self.loggedIn = True
            print(f"User {self.userName} signed in successfully")
        else:
            print("Invalid credentials, please try again or signup first")
        self.menu() 

    def writepost(self):
        if self.loggedIn:
            post = input("Enter your post content : ")
            print(f"Post '{post}' created successfully")
        else:
            print("Please signin to write a post")
        self.menu()
    
    def messagefriend(self):
        if self.loggedIn:
            friend = input("Enter your friend's name : ")
            message = input("Enter your message : ")
            print(f"Message '{message}' sent to {friend} successfully")
        else:
            print("Please signin to message a friend")
        self.menu()

chatbookobj = chatbook()        