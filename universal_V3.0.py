import subprocess as sp


def main():

    uID = 1000
    uID = uID + 1

    ulID = 'UL'+str(uID)
    print("Universal ltd.")
    input("\nPress any key to continue...")
    sp.call('clear', shell=True)

    # defining the variables that'll hold specific data of ratios
    appsConsidered = 0
    appsAproved = 0

    totPaidRatio = 0
    totEduExpenceRatio = 0

    # counters for the shortfall count and shortfall average
    shortfalcnt = 0
    aveShortfal = 0

    num = int(input("Enter the number of student application you wish to process: "))
    for i in range(1, num + 1):
        stuName = input("Enter students first name: ")
        uniName = input("Enter University name: ")
        stuGPA = float(input('Enter student GPA: '))

        print("\nFinancial Data:")
        while True:
            try:
                tuitionFee = float(input("Enter Tuition Fee: "))
                break
            except ValueError:
                print("Invalid user input.")

        while True:
            print(
                "Enter Accomodation type \nON-Campus (O) \nNear-Campus (N) \nDistance (D)")
            acomType = input().lower()  # Accommodation type
            while acomType not in ['o', 'n', 'd']:
                print("invalid accomodation type.")
                break
            else:
                break

        while True:
            try:
                textCost = float(input("Enter the cost of textbooks: "))
                break
            except ValueError:
                print("Invalid user input.")
        while True:
            try:
                misEduItems = float(
                    input("Enter the cost of miscellaneous education items: "))
                break
            except ValueError:
                print("Invalid user input.")
        while True:
            try:
                totalPaid = float(input("\nEnter the total amount paid: "))
                break
            except ValueError:
                print("Invalid user input.")

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
        shortfalcnt = shortfalcnt + 1

        # Calculating 20% of the tuition fee
        feeUp20 = (tuitionFee * 20) / 100

        if shortFall > feeUp20 or totalEduEx >= 500000.00:
            status = 'Submitted to the Scholarship Unit'
            appsAproved = appsAproved + 1
        elif totalPaid >= totalEduEx:
            status = 'Rejected'
        else:
            status = 'Short-listed for further consideration'
            appsConsidered = appsConsidered + 1

        # Calculating the average shartfall per student
        aveShortfal = aveShortfal + shortFall

        print('APPLICATION ID: {}'.format(ulID))

        print("STUDENT NAME: {}".format(stuName.capitalize()))
        print("STUDENT GPA: {}".format(stuGPA))
        print("INSTITUTION: {}".format(uniName.upper()))
        print("ACCOMODATION TYPE: ({})".format(acomType.upper()))
        print("TOTAL EXPENSES ($): {}".format(round(totalEduEx, 2)))
        print("SHORTFALL ($): {}".format(round(shortFall, 2)))
        print("\nAPPLICATION STATUS: ")
        print(status)
        print('\n')

    print("Grant Application Summer:")
    print("Menu Options - \n \
    A. Ratio of Total Ammount Paid to Total Expenses. \n \
    B. Ratio of Applications being Considered for Grants to Applications Processed. \n \
    C. Average Shortfall per Eligeble Student. \n \
    X. Exit ")
    menuOpt = input('Enter option: ').lower()

    if menuOpt == 'a':
        print("")
    elif menuOpt == 'b':
        print("")
    elif menuOpt == 'c':
        print("")
    elif menuOpt == 'x':
        quit()


if __name__ == "__main__":
    main()
