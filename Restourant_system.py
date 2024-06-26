from colorama import Fore
import time
from tqdm import tqdm 
for i in tqdm(range(100),colour='green'):
     time.sleep(0.02)	
print(Fore.GREEN,"Complete.")
a=1
while a==1:
    print(Fore.YELLOW,"                                       *************************           ")
    print("                                        ||**AL MISHARY RASHID**||            ")
    print(Fore.YELLOW,"                                       *************************                        ")
    print("  \n")
    print("                |*******************************************************************|                   ")
    print("                |***********||            WELCOME TO OUR HOTEL        *||***********|                ")
    print("                |*******************************************************************|                  ")
    print("                |  **************************************************************** |                 ")
    print("                |   ********||*****************************************||*********  |                   ")
    print("                |    *******||*****************************************||********   |                   ")
    print("                |     ******|| 1--> For Checking Menu                 *||******     |                   ")
    print("                |      *****||*****************************************||*****      |                   ")
    print("                |       ****|| 2--> For Ordering Menu                 *||****       |                   ")
    print("                |        ***||*****************************************||***        |                   ")
    print("                |         **|| 3--> For Checking Inventory            *||**         |                   ")
    print("                |          *||*****************************************||*          |                   ")
    print("                |         **|| 4--> For Giving Reviews                *||**         |                   ")
    print("                |        ***||*****************************************||***        |                   ")
    print("                |      *****|| 5--> For Checking Your Order           *||******     |                   ")
    print("                |       ****||*****************************************||*****      |                   ")
    print("                |      *****|| 6--> For Exit The Menu                 *||******     |                   ")
    print("                |     ******||*****************************************||*******    |                   ")
    print("                |    *******||*****************************************||********   |                   ")
    print("                |  *********||*****************************************||*********  |                   ")
    print("                | **********||*****************************************||********** |                   ")
    print("                |***********||*****************************************||***********|                   ")
    print("                |***********||*****************************************||***********|                   ")
    print("                |*******************************************************************|                   ")
    class menu:
        pass
    class entree(menu): 
        def data_base():
            print(Fore.MAGENTA,"                                              Enjoy Our Service \n")
            file = open("Database.txt","r")
            print(file.read())
    try:
        operation = int(input("                 Choose Your Operation: "))
        if operation == 1:
            class dessert(entree):
                @staticmethod
                def append_data_base():
                    file = open("Database.txt","a")
                    file.close()
                append_data_base()
                entree.data_base()
        elif operation == 2:
            class Order:
                def __init__(self,user,tableId,payment):
                    self.user = user
                    self.tableId = tableId
                    self.menu_item =  []
                    self.payment = payment             
                    print(self.user)
                    print(self.tableId)
                    print(self.menu_item)
                    print(self.payment)
                for x in range(50):
                    try:
                        print(Fore.CYAN,"                                      Choose Your Menu ")
                        print("                                       | 1 | For Booking Your Order ")
                        print("                                       | 2 | For Exit ")
                        opt = int(input("                  Choose Your Option : "))
                        if opt == 1:
                            tableId = int(input("              | Table Id :"))
                            user = input("                     | Enter User Name :")
                            menu_item = input("                | Select item you want to order : ") 
                            payment = int(input("              | Enter Your Payment :"))
                            file = open("data.txt","a")
                            from tinydb import TinyDB
                            db = TinyDB('data.txt')
                            db.insert({'TableId ': tableId, 'Name ': user, 'Menu Items ':menu_item,'Payment':payment})
                        elif(opt==2):
                            print("                             Your Order has been submitted.")
                            print("                             Soon you will Receive it.")
                            break
                    except ValueError:
                        print("Something else went wrong.Please Enter Valid Input.")
        elif operation ==3:
            class inventory:
                def search_Item_in_file(file_path, Item):
                    with open(file_path, 'r') as file:
                        for line in file:
                            if Item in line:
                                return line
                    return None
                file_path = 'Inventory.txt'  
                Item_to_search = input("Enter a Item to search: ")

                result = search_Item_in_file(file_path, Item_to_search)

                if result is not None:
                    print("Item found in the Inventory:", result)
                else:
                    print("Item not found in the Inventory.")
        elif(operation==4):
            class Reviews:
                def __init__(self, location, environment, security, facilities, cleanliness, management, behaviour):
                    self.location = location
                    self.environment = environment
                    self.security = security
                    self.facilities = facilities
                    self.cleanliness = cleanliness
                    self.management = management
                    self.behaviour = behaviour    

                def display_data(self):
                    print(Fore.GREEN,"Location: ", self.location)
                    print("Environment: ", self.environment)
                    print("Security: ", self.security)
                    print("Facilities: ", self.facilities)
                    print("Cleanliness: ", self.cleanliness)
                    print("Management: ", self.management)
                    print("Behaviour: ", self.behaviour)

            location = input("Is location is good or not? ")
            environment = input("How do you feel about the environment of Restaurent? ")
            security = input("Are you feel secure or not in Restaurent? ")
            facilities = input("Does the Restaurent provides all types of facilities or not? ")
            cleanliness = input("Is Restaurent is clean or Not? ")
            management = input("Is management are good or not? ")
            behaviour = input("Do you like the behaviour of Restaurent faculty or not? ")

            view = Reviews(location, environment, security, facilities, cleanliness, management, behaviour)
            view.display_data()    
        elif operation ==5:
            class checkorder:
                def search_order_in_file(file_path, Item):
                    with open(file_path, 'r') as file:
                        for line in file:
                            if Item in line:
                                return line
                    return None
                file_path = 'data.txt'  
                order_to_search = input("Enter Name to search Your Order Description : ")

                result = search_order_in_file(file_path, order_to_search)

                if result is not None:
                    print("Order Description is found :", result)
                else:
                    print("Order not found .")
        elif(operation==6):
            print("                                         Hope You Enjoy Our Service. ")
            print("                                           Thanks For Choosing Us. ")
            break        
    except ValueError :
        print("Something else went wrong.Please Enter Valid Input.")
    finally :
        print("                                              Thanks For Coming \n")
    