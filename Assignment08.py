# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# ChrisPerry, 11.26.2019, Initial Edits
# ChrisPerry, 11.27.2019, Final Edits
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #

# Declare variables and constants
strFileName = "products.txt" 
lstOfProductObjects = [] 
objFile = None   
dicRow = {}  
strChoice = ""  
strProduct = ""
strPrice = ""

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ChrisPerry, 11.26.2019, Initial Edits
        ChrisPerry, 11.27.2019, Final Edits
    """
    pass

    # -- Constructor --
    def __init__(self, product_name, product_price):
        #-- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    # -- Properties --
    # product_name

    @property 
    def product_name(self):  # (getting or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter
    def product_name(self, value):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # product_price
    @property
    def product_price(self):  # (getting or accessor)
        return str(self.__product_price).title()  # Title case

    @product_price.setter  # The name needs to match the property's name
    def product_price(self, value):  # (setter or mutator)
        self.__product_price = value

    def __str__(self):
        return self.product_name + ',' + self.product_price
# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ChrisPerry, 11.26.2019, Initial Edits
        ChrisPerry, 11.27.2019, Final Edits
    """
    pass
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Product": data[0].strip(), "Price": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        """
        Desc - Writes data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: nothing
        """
        pass 

        objFile = open(file_name, "w")
        for dicRow in list_of_rows:  # Write each row of data to the file
            objFile.write(dicRow["Product"] + "," + dicRow["Price"] + "\n")
        objFile.close()

    @staticmethod
    def AddRowToList(product, price, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows
        :param product: (string) with name of product:
        :param price: (string) with name of price level:
        :param list_of_rows: (list) you want filled with file data:
        :return: nothing
        """
        dicRow = {"Product": product, "Price": price}  # Create a new dictionary row
        list_of_rows.append(dicRow)  # Add the new row to the list/table

# Processing  ------------------------------------------------------------- #

class IO:
    """ A class for performing Input and Output """
    pass
    @staticmethod
    def OutputMenuItems():
        """  Print a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add a new product.
        3) Save Data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def InputMenuChoice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def ShowCurrentItemsInList(list_of_rows):
        """ Shows the current items in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current products and their corresponding prices are: *******")
        for row in list_of_rows:
            print(row["Product"] + " (" + row["Price"] + ")")
        print("************************************************************************")
        print()

    @staticmethod
    def addItem():
        """ Adds item based off user input to list table
        
        :param strTask: Task name based on user input
        :param strPriority: Priority name based on user input
        :param list_of_rows: (list) of rows you want to display
        :return: task and priority added to list
        """
        # Step 3.2.a - Ask user for new task and priority
        strProduct = str(input("What is the product name? ")).strip()  # Get product name from user
        strPrice = str(input("What is the product price? ")).strip()  # Get product price from user
        objP1 = Product(strProduct, strPrice)
        print() 

        # Step 3.2.b  Add item to the List/Table
        # Convert to function for processing
        FileProcessor.AddRowToList(objP1.product_name, objP1.product_price, lstOfProductObjects)
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table

    @staticmethod
    def saveFiles():
        """ Removes item based off user input from list table
        
        :param strFileName: name of local file
        :param list_of_rows: (list) of rows you want to display
        :return: none
        """
        #Step 3.4.a - Show the current items in the table
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table

        #Step 3.4.b - Ask if user if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            # Convert to function for processing
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:  # Let the user know the data was not saved
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")



# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from products.txt.
FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data upon load

# Step 2 - Display a menu of choices to the user
while(True):
    IO.OutputMenuItems()  # Shows menu
    strChoice = IO.InputMenuChoice()  # Get menu option

    # Step 3 - Process user's menu choice
    # Step 3.1 Show current data
    if (strChoice.strip() == '1'):
        IO.ShowCurrentItemsInList(lstOfProductObjects)  # Show current data in the list/table
        continue  # to show the menu

    # Step 3.2 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        IO.addItem()
        continue  # to show the menu

    # Step 3.3 - Ask user if they want to save tasks to the local file
    elif(strChoice == '3'):
        IO.saveFiles()
        continue  # to show the menu

    # Step 3.4 - Breaks the loop and exits the script
    elif(strChoice == '4'):
        break  # and exit

# Main Body of Script  ---------------------------------------------------- #
