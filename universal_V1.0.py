import subprocess as sp 

def ulmain():
    print("Universal ltd.")
    input("\nPress any key to continue...")
    sp.call('clear', shell = True) 

    print("Enter Student data:")
    stuname = input("Enter Students Name: ")
    uniName = input("Enter University name: ")

    print("\nFinancial Data:")
    tuitionFee = float(input("Enter Tuition Fee: "))
    boardCost = float(input("Enter boarding cost: "))
    textCost = float(input("Enter the cost os textbooks: "))
    misEduItems = float(input("Enter cost miscellaneous education items: "))
    totalPaid = float(input("\nEnter the total amount paid: "))

    totalEx = tuitionFee + boardCost + textCost + misEduItems 

    shortFall = totalEx - totalPaid

    print("Student Profile")
    print(f"\nSTUDENT NAME: {stuname.capitalize()}")
    print(f"INSTITUTION: {uniName.capitalize()}")
    print(f"TOTAL EXPENSES ($): {totalEx:.3}")
    print(f"SHORTFALL ($): {shortFall:.3}")


if __name__ == "__main__":
    ulmain()
