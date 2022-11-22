import csv
import datetime
import re

while True:
    selection = int(input(
        "You may select one of the following:" + '\n' + "1) List available cars" + '\n' + "2) Rent a car" + '\n' + "3) Return a car" + '\n' + "4) Count the money" + '\n' + "0) Exit" + '\n' + "What is your selection?" + '\n'))
    if selection == 1:
        print("The following cars are available:")
        availableVehicleList = []
        rentedCarRegisterIdList = []
        with open('rentedVehicles.txt', 'r') as rentedVehicles:
            rentedVehiclesCsv = csv.reader(rentedVehicles)
            for i in rentedVehiclesCsv:
                if len(i) != 0:
                    rentedCarRegisterIdList.append(i[0])
        rentedVehicles.close()
        with open('Vehicles.txt', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for j in csvreader:
                if j[0] not in rentedCarRegisterIdList:
                    availableVehicleList.append(j)
            for row in availableVehicleList:
                if len(row) == 4:
                    print('* Reg. nr: ' + row[0] + ', ' + 'Model: ' + row[1] + ', ' + 'Price per day: ' + row[
                        2] + '\n' + 'Properties: ' + row[3])
                elif len(row) == 5:
                    print('* Reg. nr: ' + row[0] + ', ' + 'Model: ' + row[1] + ', ' + 'Price per day: ' + row[
                        2] + '\n' + 'Properties: ' + row[3] + ', ' + row[4])
                else:
                    print('* Reg. nr: ' + row[0] + ', ' + 'Model: ' + row[1] + ', ' + 'Price per day: ' + row[
                        2] + '\n' + 'Properties: ' + row[3] + ', ' + row[4] + ', ' + row[5])

        csvfile.close();

    if selection == 2:
        regNumber = input("Give the register number of the car your want to rent:" + '\n')
        modelList = []
        with open('Vehicles.txt', 'r') as csvfile:

            csvreader = csv.reader(csvfile)
            for row in csvreader:
                modelList.append(row[0])
        csvfile.close();
        if regNumber in modelList:
            birthday = input("Please enter you birthday in the form DD/MM/YYYY:" + '\n')
            d = datetime.date(int(birthday[6:]), int(birthday[3:5]), int(birthday[0:2]))
            # //////////////////////////////////////////////////////////////////////////////
            if type(d) is not datetime.date:
                print("birthday input is wrong")
            else:
                # print("birthday input is ok")
                # //////////////////////////////////////////////////////////////////////////////
                if 2022 - int(birthday[6:]) >= 18:
                    # print("age is ok")
                    with open('Customers.txt', 'r') as csvfile:
                        csvreader = csv.reader(csvfile)
                        birthdayList = []
                        for row in csvreader:
                            birthdayList.append(row[0])
                    csvfile.close()
                    if birthday in birthdayList:
                        with open('Customers.txt', 'r') as csvfile:
                            csvreader = csv.reader(csvfile)
                            for a in csvreader:
                                if birthday == a[0]:
                                    firstName = a[1]
                                    print("Hello", firstName)
                        csvfile.close()
                    else:
                        firstName = input("Please enter your firstName: ")
                        lastName = input("Please enter your lastName: ")
                        while True:
                            # GET FROM INTERNET
                            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                            email = input("Please enter your email address: ")
                            if (re.fullmatch(regex, email)):
                                break
                            else:
                                print("Invalid Email")
                        with open('Customers.txt', 'a') as file1:
                            inputStr = "\n" + birthday + "," + firstName + "," + lastName + "," + email
                            file1.write(inputStr)
                        csvfile.close()
                        print("Hello", firstName)
                    x = str(datetime.datetime.now())
                    # exportTime = x[0:4] + "/" + x[5:7] + "/" + x[8:10] + " " + x[11:16]
                    exportTime = x[8:10] + "/" + x[5:7] + "/" + x[0:4] + " " + x[11:16]
                    rentString = "\n" + regNumber + "," + birthday + "," + exportTime
                    with open('rentedVehicles.txt', 'a') as file2:
                        file2.write(rentString)
                    csvfile.close()
                    print("You rented the car", regNumber)
                else:
                    print("age is not ok")
        else:
            print("This car is unavailable")
        csvfile.close()
    if selection == 3:
        rentedRegNumber = input("Give the register number of the car your want to return:" + "\n")
        modelList = []
        # ////////Check regNumber in rentedVehicles list
        with open('rentedVehicles.txt', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) != 0:
                    modelList.append(row[0])
        csvfile.close()
        if rentedRegNumber in modelList:
            # //////////Get car Price
            with open('Vehicles.txt', 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if rentedRegNumber in row[0]:
                        price = row[2]
            csvfile.close()
            # //////////////Get rent Date
            with open('rentedVehicles.txt', 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if len(row) != 0:
                        if rentedRegNumber in row[0]:
                            userRentBirthday = row[1]
                            rentDatetime = row[2]
                            rentDate = rentDatetime[0:10]
                        # print(rentDate)
            csvfile.close()
            # /////////////////Date calculation
            today = datetime.date.today()
            tempdate = str(rentDate)
            primaryRentDay = tempdate.replace("/", ",")
            year = primaryRentDay[6:10]
            month = primaryRentDay[3:5]
            day = primaryRentDay[0:2]
            if int(day) < 10:
                day = day.replace("0", "")
            if int(month) < 10:
                month = month.replace("0", "")
            finalDate = year + "," + month + "," + day
            someday = datetime.date(int(year), int(month), int(day))
            sumOfDay = (today - someday).days
            # print(sumOfDay)
            # /////////////////////////Calculate sum price
            sumPrice = float(sumOfDay) * float(price)
            # print("The total amount of money is", "%.2f" % round(sumPrice, 1), "euros")
            print("The rent lasted", sumOfDay , "days and the cost is", "%.2f" % round(sumPrice, 1), "euros")
            # ////////////Remove car from rented List
            temCarList = []
            with open('rentedVehicles.txt', 'r', newline='') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    temCarList.append(row)
                    for field in row:
                        if row[0] == rentedRegNumber:
                            temCarList.remove(row)
                            break
            csvfile.close()
            with open('rentedVehicles.txt', 'w', newline='') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(temCarList)
            writeFile.close()
            # ////////////////Add to Transactions
            with open('transActions.txt', 'a') as file1:
                x = str(datetime.datetime.now())
                # exportTime = x[0:4] + "/" + x[5:7] + "/" + x[8:10] + " " + x[11:16]
                exportTime = x[8:10] + "/" + x[5:7] + "/" + x[0:4] + " " + x[11:16]
                inputString = rentedRegNumber + "," + userRentBirthday + "," + rentDatetime + "," + exportTime + "," + str(
                    sumOfDay) + "," + "%.2f" % round(sumPrice, 1) + "\n"
                file1.write(inputString)
            csvfile.close()
        else:
            print("This regNumber is not available")

    if selection == 4:
        priceList = []
        totalSumPrice = 0
        with open('transActions.txt', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                priceList.append(row[5])
        csvfile.close()
        for i in priceList:
            totalSumPrice = float(i) + float(totalSumPrice)
        print("The total amount of money is", "%.2f" % round(totalSumPrice, 1), "euros")
    if selection == 0:
        break
