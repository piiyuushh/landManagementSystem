import datetime
from read import readfile
from write import rentBill
from write import returnBill
#from read import display
      
class Land:
    def __init__(self, landId, kittaNo, location, direction, anna, price, availibilityStatus):
        self.landId = landId
        self.kittaNo = kittaNo
        self.location = location
        self.direction = direction
        self.anna = anna
        self.price = price
        self.availibilityStatus = availibilityStatus
        
#function to rent land
def rentland():
    totalAmount = 0
    while True:
        availableLands = [land for land in landList if land.availibilityStatus == "Available"]
        if not availableLands:
            print("No more lands available for rent.")
            break
        for land in availableLands:
            print("Available lands for rent \n")
            print(f"Land ID: {land.landId}, Location: {land.location}, Price: {land.price}")
        try:
            ent = int(input("Enter the land ID of the land you want to rent: "))
            landToRent = next((land for land in availableLands if land.landId == ent), None)
            if landToRent:
                print("You are renting a land.")
                name = input("Enter your name: ")
                entryTime = str(datetime.datetime.now().minute) + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond)
                print("Hi",name,"you entered at",entryTime)
                months = int(input("Enter the months you want to rent land for: "))
                rentAmount = months * landToRent.price
                totalAmount += rentAmount
                print("Total Amount: ",totalAmount)
                print("Land rented successfully!")
                print("Land availibility status changed to not available.")
                print("Bill is also created and saved.")
                landToRent.availibilityStatus = "Not Available"
                
                try:
                    with open("land.txt", "r") as file:
                        lines = file.readlines()

                    for i in range(len(lines)):
                        words = lines[i].split()
                        if str(land.availibilityStatus) in words:
                            if "Not Available" in lines[i]:
                                lines[i] = lines[i].replace("Available", "Not available")
                            else:
                                print(f"Line {i} does not contain 'Available'")
                            break
                    else:
                        print(f"No line contains {land.availibilityStatus}")

                    with open("land.txt", "w") as file:
                        file.writelines(lines)
                except Exception as e:
                    print(f"An error occurred: {e}")
                
                #creating a bill for rented lands
                rentBill(name, entryTime, landToRent, months, rentAmount)
                  
            else:
                print("Invalid land ID. Check the chart again.")
        except ValueError:
            print("Invalid input. Please enter a valid Land ID.")
            continue
        rentmore = input("Do you want to rent more land? (yes/no): ")
        if rentmore.lower() != "yes":
            print("Thank you for renting land.")
            break
        else:
            print("Thank you for using the land rental system.")
            print("Total amount to be paid: ", totalAmount)
            break
    menu_selection()
# function to return land    
def returnLand():
    while True:
        rentedLands = [land for land in landList if land.availibilityStatus == "Not Available"]
        if not rentedLands:
            print("No lands are rented.")
            break
        for land in rentedLands:
            print("lands to return \n")
            print(f"Land ID: {land.landId}, Location: {land.location}, Price: {land.price}")
        try:
            ent = int(input("Enter the land ID of the land you want to return: "))
            landToReturn = next((land for land in rentedLands if land.landId == ent), None)
            if landToReturn:
                print("You are returning a land.")
                name = input("Enter your name: ")
                entryTime = str(datetime.datetime.now().minute) + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond)
                duration = int(input("Enter the duration of the rent: "))
                extraMonths = int(input("Enter the extra months of the rented land: "))
                if extraMonths > 0:
                    
                    fine = 0.1 * landToReturn.price * extraMonths
                    TotalAmount = landToReturn.price * extraMonths + fine
                    print(f"Fine imposed: {fine}")
                    print("Rented Amount payment:", TotalAmount)
                else:
                    fine = 0
                print("Land returned successfully!")
                print("land availibility status changed to available.")
                print("Bill is also created and saved.")
                landToReturn.availibilityStatus = "Available"
                
                try:
                    with open("land.txt", "r") as file:
                        lines = file.readlines()

                    for i in range(len(lines)):
                        words = lines[i].split()
                        if str(land.landId) in words:  # Change this line
                            if "Not Available" in lines[i]:
                                lines[i] = lines[i].replace("Not Available", "Available")
                            else:
                                print(f"Line {i} does not contain 'Not Available'")
                            break
                    else:
                        print(f"No line contains {land.landId}")  # Change this line

                    with open("land.txt", "w") as file:
                        file.writelines(lines)
                except Exception as e:
                    print(f"An error occurred: {e}")
                
                # Create a bill for returned lands
                returnBill(name, entryTime, landToReturn, duration, fine, TotalAmount)
                
            else:
                print("Invalid land ID. Check the chart again.")
        except ValueError:
            print("Invalid input. Please enter a valid Land ID.")
            continue
        returnMore = input("Do you want to return more land? (yes/no): ")
        if returnMore.lower() != "yes":
            print("Thank you for returning land.")
            break
    menu_selection()      
# list for lands
landList = [
    Land(1, 101, "Kathmandu", "North", 4, 50000, "Available"),
    Land(2, 102, "Pokhara", "East", 5, 60000, "Not Available"),
    Land(3, 103, "Lalitpur", "South", 10, 100000, "Available"),
    Land(4, 104, "Bhaktapur", "West", 12, 80000, "Available"),
    Land(5, 105, "Chitwan", "North", 8, 15000, "Not Available"),
    ]
# graphical welcome screen            
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("   Welcome to land management system. Follow the given instructions to proceed.")
print("-------------------------------------------------------------------------------")
# function to display menu
def menu_selection():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("   Press '1' to rent a land.")
    print("   Press '2' to return a land.")
    print("   Press '3' to exit.")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    ent = int(input("Enter your choice: "))
    try:
        
        if ent == 1:
            print("----------------------------------------------------")
            print("|              You are renting a land               |")
            print("----------------------------------------------------")
            #display()
            rentland()
        elif ent == 2:
            print("----------------------------------------------------")
            print("|              You are returning a land            |")
            print("----------------------------------------------------")
            returnLand()
        elif ent == 3:
            print("----------------------------------------------------")
            print("|  Thank you for using our land rental system.     |")
            print("--------------------------------------------------")
        else:
            print("Invalid input. Please enter a valid choice.")
            menu_selection()
    except ValueError:
        print("Invalid input. Please enter a valid choice.")
            
        
# calling the menu function             
menu_selection()     
