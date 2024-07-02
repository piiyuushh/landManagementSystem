#function to write bill of rented lands

def rentBill(name,entryTime,landToRent,months,rentAmount):
    file = open(f"{name}_{entryTime}_RentBill.txt","a")
    file.write("Techno Property Nepal\n\n")
    file.write("Rented Land Bill\n\n")
    file.write(f"Customer name: {name}\n")
    file.write(f"Bill no: {entryTime}\n")
    file.write(f"Land Id: {landToRent.landId}\n")
    file.write(f"Location: {landToRent.location}\n")
    file.write(f"Price of rent: {landToRent.price}\n")
    file.write(f"Duration of rented lands in months: {months}\n")   
    file.write(f"Total amount: {rentAmount}\n")

#function to write bill of returned lands
def returnBill(name,entryTime,landToReturn,duration,fine,TotalAmount):
    file = open(f"{name}_{entryTime}_ReturnBill.txt","a")
    file.write("Techno Property Nepal\n\n")
    file.write("Returned Land Bill\n\n")
    file.write(f"Name: {name}\n")
    file.write(f"Land ID: {landToReturn.landId}\n")
    file.write(f"Location: {landToReturn.location}\n")
    file.write(f"Price: {landToReturn.price}\n")
    file.write(f"Returned Duration: {duration}\n")
    file.write(f"Fine: {fine}\n")
    file.write(f"Total Amount: {TotalAmount}\n")