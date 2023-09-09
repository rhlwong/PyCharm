class User:

# Constructor
# def __init__(self):   <<< it is a constructor, call everytime when instance created
# __ __ initialize the attribute
    def __init__(self, seats):
        print("create instance")
        self.seats = seats

    def enter_seats_mode(self): # self mean , the obj that created by the class itself
        self.seats = 2

myUser = User(7)
civic = User(5)
civic.enter_seats_mode()
myUser.id = "001"
print(myUser.seats)
print(civic.seats)
