import subprocess as sp


def main():

    accomCost = 0

    print('Universal ltd.')
    input('\nPress any key to continue...')
    sp.call('clear', shell=True)

    print('Enter student data:')
    stuName = input('Enter student name: ')
    stuID = input('Enter Student ID: ')
    stuGPA = float(input('Enter student GPA: '))
    if stuGPA <= 0.0 or stuGPA > 4.0:
        print('Invalid student GPA.')
        exit()
    elif stuGPA <= 2.7:
        print("GPA's less than 2.7 are automatically rejected.")
        exit()

    uniName = input('Enter University Name: ')

    while True:
        print("Enter Accomodation type \nON-Campus (O) \nNear-Campus (N) \nDistance (D)")

        acomType = input().lower()  # Accommodation type
        while acomType not in ['o', 'n', 'd']:
            print("invalid accomodation type.")
            break
        else:
            break

    print('\nFinancial Date:')
    tuitionFee = float(input("Enter Tuition Fee: "))
    # boardCost = float(input("Enter boarding cost: "))
    textCost = float(input("Enter the cost os textbooks: "))
    misEduItems = float(input("Enter cost miscellaneous education items: "))
    totalPaid = float(input("\nEnter the total amount paid: "))

    # Accomodation cost
    if acomType == 'o':
        accomCost = (tuitionFee * 15) / 100
    elif acomType == 'n':
        accomCost = (tuitionFee * 20) / 100
    elif acomType == 'd':
        accomCost = (tuitionFee * 30) / 100

    # Calculating the students overall expenses
    totalEduEx = tuitionFee + textCost + misEduItems + accomCost
    # Calculating the students shortfall
    shortFall = totalEduEx - totalPaid

    # Calculating 20% of the tuition fee
    feeUp20 = (tuitionFee * 20) / 100

    if shortFall > feeUp20 or totalEduEx >= 500000.00:
        status = 'Submitted to the Scholarship Unit'
    elif totalPaid >= totalEduEx:
        status = 'Rejected'
    else:
        status = 'Short-listed for further consideration'

    print("\nStudent Profile")
    print("\nSTUDENT NAME: {}".format(stuName.capitalize()))
    print("STUDENT ID: {}".format(stuID))
    print("STUDENT GPA: {}".format(stuGPA))
    print("INSTITUTION: {}".format(uniName.upper()))
    print("ACCOMODATION TYPE: ({})".format(acomType.upper()))
    print("TOTAL EXPENSES ($): {}".format(round(totalEduEx, 2)))
    print("SHORTFALL ($): {}".format(round(shortFall, 2)))
    print("\nAPPLICATION STATUS: ")
    print(status)


if __name__ == "__main__":
    main()
