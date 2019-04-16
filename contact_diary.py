"""
    Python Contact Diary
"""

import csv

'''
    App Initialization 
    Checking for data file
'''
data_file = "DiaryData.csv"

#initializing gobal variables
user_input = ""
data = []

'''
    UI Class
    it consist of all command ui
'''
class UI:

    '''
        Starting and Main User Interface of the app
        It displays all the command of the app
    '''
    def mainUI():
        global user_input
        print("\n{:^50}".format("Contact Diary"))
        print("{:-^50}".format("-"))
        print("    {:<7} | {}".format("Show","Show all entries of Diary."))
        print("    {:<7} | {}".format("New","Add new entry in Diary."))
        print("    {:<7} | {}".format("Search","Search contact in Diary."))
        print("    {:<7} | {}".format("Exit","Close the application."))
        user_input = input("--> ")

    '''
        New Command UI
    '''
    def newUI():
        print("\n{:^50}".format("New Entry"))
        print("{:-^50}".format("-"))
        print("    {:<10} | {}".format("Name","Enter Name"))
        print("    {:<10} | {}".format("Phone No","Enter Phone Number"))
        print("    {:<10} | {}".format("Address","Enter Address"))

    def searchUI():
        print("\n{:^50}".format("Search Entry"))
        print("{:-^50}".format("-"))
        print("    {}".format("Enter command and then value for searching give as many detail you know\n"))
        print("    {:<10} | {}".format("N","Enter Name "))
        print("    {:<10} | {}".format("PN","Enter Phone Number"))
        print("    {:<10} | {}".format("A","Enter Address"))
        print("    {:<10} | {}".format("S","Start Searching"))
        print("    {:<10} | {}".format("Q","Go Back"))
           

'''
    CommandFunction class
    It has function that perform commands
'''
class CommandFunction:

    '''
        New Command function
    '''
    def newEntry():
        UI.newUI()
        name = input("\nName : ")
        number = input("Phone No : ")
        address = input("Address : ")
        file = open(data_file,"a+")
        writer = csv.writer(file)
        writer.writerow([name,number,address])
        file.close()



    def showEntry():
        print("\n{:^50}".format("All Entries"))
        print("{:-^50}".format("-"))
        print("{:^15}|{:^15}|{:^15}".format("Name","Phone No","Address"))
        print("{:-^50}".format("-"))
        file = open(data_file,"r")
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 0:
                continue
            print("{:^15}|{:^15}|{:^15}".format(row[0],row[1],row[2]))

        file.close()


    def searchEntry():
        UI.searchUI()
        def getData():
            global data
            global user_input
            user_input = input("--> ")
            if user_input == "Q":
                pass
            if user_input != "S":
                if user_input == "N":
                    data.append(input("Name : "))
                    getData()
                elif user_input == "PN":
                    data.append(input("Phone No : "))
                    getData()
                elif user_input == "A":
                    data.append(input("Address : "))
                    getData()
                else:
                    print("Invalid Command")
                    getData()
            else:
                print("Searching.........")
                print(data)
                file = open(data_file,"r")
                reader = csv.reader(file)
                for row in reader:
                    check_data = 0
                    for col in row:
                        for i in range(len(data)):
                            if col in data[i]:
                                check_data += 1
                    if check_data == len(data):
                        print("{:^15}|{:^15}|{:^15}".format(row[0],row[1],row[2]))
                
                            
            
        getData()
                    
while True:
    UI.mainUI()
    if user_input == "Show":
        #------
        CommandFunction.showEntry()
    elif user_input == "New":
        #-------
        CommandFunction.newEntry()
    elif user_input == "Search":
        #-------
        CommandFunction.searchEntry()
    elif user_input == "Exit":
        print("Existing .........\n")
        exit()
    else:
        print("Invalid Command ")
