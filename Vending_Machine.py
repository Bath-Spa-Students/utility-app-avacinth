# Welcome message
print ("""
                                                                             █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
                                                                             ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄
       
                                                                                            𝐭𝐨   
                                                                             
                                                  █▀▄▀█ █░█ █▄░█ █▀▀ █░█   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
                                                  █░▀░█ █▄█ █░▀█ █▄▄ █▀█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄""")

print("""
                                                  -----------------------------------------------------------------------------------   
                                          
                                                                                  █▀▄▀█ █▀▀ █▄░█ █░█
                                                                                  █░▀░█ ██▄ █░▀█ █▄█ 
      """)
# Item's category such as Item Name, Code, Price, and Stock stored in a Nested Dictionary
A_items = [
    {
        "Item_Name": "Water",
        "Code": "A1",
        "Price": 1.00,
        "Stock": 5
    },
    {
        "Item_Name": "Coke",
        "Code": "A2",
        "Price": 3.00,
        "Stock": 2
    },
    {
        "Item_Name": "Milk",
        "Code": "A3",
        "Price": 2.00,
        "Stock": 6
    },
    {
        "Item_Name": "Apple Juice",
        "Code": "A4",
        "Price": 2.00,
        "Stock": 8
    },
    {
        "Item_Name": "Coconut Juice",
        "Code": "A5",
        "Price": 3.00,
        "Stock": 6
    }
]

B_items = [
    {
        "Item_Name": "Lay's Classic",
        "Code": "B1",
        "Price": 3.00,
        "Stock": 5
    },
    {
        "Item_Name": "Popcorn",
        "Code": "B2",
        "Price": 4.00,
        "Stock": 0
    },
    {
        "Item_Name": "Cheetos",
        "Code": "B3",
        "Price": 3.00,
        "Stock": 6
    },
    {
        "Item_Name": "Doritos",
        "Code": "B4",
        "Price": 3.00,
        "Stock": 3
    },
    {
        "Item_Name": "Oreo",
        "Code": "B5",
        "Price": 2.00,
        "Stock": 4
    }
]

C_items = [
    {
        "Item_Name": "Resses",
        "Code": "C1",
        "Price": 2.00,
        "Stock": 4
    },
    {
        "Item_Name": "Hersheys",
        "Code": "C2",
        "Price": 2.00,
        "Stock": 9
    },
    {
        "Item_Name": "Snickers",
        "Code": "C3",
        "Price": 2.00,
        "Stock": 6
    },
    {
        "Item_Name": "Galaxy",
        "Code": "C4",
        "Price": 2.00,
        "Stock": 8
    },
    {
        "Item_Name": "Twix",
        "Code": "C5",
        "Price": 2.00,
        "Stock": 0
    }
]

# Function to print the table of items
def print_table(items):
    header = ["Item", "Code", "Price", "Stock"]
    row_format = "{:<18} {:<18} {:<16} {:<16}"

    centered_header = row_format.format(*header).center(192)
    print(centered_header)
    print("                                                          -------------------------------------------------------------------- ")

    for item in items:
        # Center each row
        centered_row = row_format.format(item["Item_Name"], item["Code"], item["Price"], item["Stock"]).center(192)
        print(centered_row)

# Function to print section title with separator line
def print_section_title(title):
    line = "-" * 68
    formatted_title = f"{title.center(185)}\n{line.center(184)}"  #line under item label ex. drinks
    print(formatted_title)

# Print items in each category
print_section_title("𝑫 𝑹 𝑰 𝑵 𝑲 𝑺​​​​​")
print_table(A_items)

print_section_title("𝑪 𝑯 𝑰 𝑷 𝑺")
print_table(B_items)

print_section_title("𝑺 𝑾 𝑬 𝑬 𝑻 𝑺")
print_table(C_items)

# Function to start the vending machine
def start():
    PURPLE = '\033[95m'
    BLUE = '\033[94m'

    while True:
        # User input to get the selected item code
        input_user = input(f"\nEnter the code of the product you want to buy (or 'exit' to end): ") 
    
        if input_user == 'exit': # The user wants to exit the vending machine
            print("""-------------------------------------------------------------------- 
              Thank you for using Munch Vending Machine. Have a great day!""")
            break

        selected_item = None
        for item in A_items + B_items + C_items:
            if item['Code'] == input_user:
                selected_item = item
                break

        if selected_item['Stock'] == 0: # The user selected an item that is out of stock
            print("""-------------------------------------------------------------------------
              
Sorry, this item is out of stock. Please choose another product.
            """)
            continue
        
        print ("-------------------------------------------------------------------------")
        print(f"\nYou have selected: {selected_item['Item_Name']}")
        print(f"Price: {selected_item['Price']}")
        print(f"Stock: {selected_item['Stock']}")

        # Get user input for cash insertion
        insert_cash = float(input(f"\nPlease insert {selected_item['Price']}: "))  

        import sys
        # Calculate change
        change = insert_cash - selected_item['Price']
        print("\n--------------------------------------------------")
        print(f"\n{PURPLE}{selected_item['Item_Name']} has been dispensed\033[0m")
        print ("\nYour remaining balance is AED", change)

        input("\nPress Enter...")

        # Suggestions for each item
        if selected_item['Item_Name'] == "Coke":
            suggestion_item = B_items[0]
            print(f"""
--------------------------------------------------

{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Milk":
            suggestion_item = B_items[4]
            print(f"""
--------------------------------------------------
          
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Apple Juice":
            suggestion_item = B_items[1]
            print(f"""
--------------------------------------------------

{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Coconut Juice":
            suggestion_item = B_items[3]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Lay's Classic":
            suggestion_item = A_items[1]
            print(f"""
--------------------------------------------------
          
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Popcorn":
            suggestion_item = A_items[3]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Cheetos":
            suggestion_item = A_items[1]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Doritos":
            suggestion_item = A_items[4]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Oreo":
            suggestion_item = A_items[4]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Resses":
            suggestion_item = A_items[1]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Hersheys":
            suggestion_item = A_items[2]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Snickers":
            suggestion_item = B_items[1]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Galaxy":
            suggestion_item = A_items[1]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        elif selected_item['Item_Name'] == "Twix":
            suggestion_item = A_items[1]
            print(f"""
--------------------------------------------------
                  
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
            print(f"\nThis item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

        suggestion = input("\nDo you want to buy this item? (yes/no): ")

        insert_cash2 = 0

        if suggestion == 'yes':
            #If the balance of money is not enough
            if change < suggestion_item['Price']: 
                insert_cash2 = float(input(f"\nYou need to insert {suggestion_item['Price'] - change} AED more: "))
                #If the balance of money meets the needed item price
                if change + insert_cash2 >= suggestion_item['Price']:
                    print("\n--------------------------------------------------")
                    print(f"\n{PURPLE}{suggestion_item['Item_Name']} has been dispensed\033[0m")
                
                    yes_suggestion = ((change + insert_cash2) - suggestion_item['Price'])
                    print(f"\nPlease get your remaining balance of AED", yes_suggestion)

            #If the balance of money is equal to or more than the suggested item price
            elif change >= suggestion_item['Price']:
                print("\n--------------------------------------------------")
                print(f"\n{PURPLE}{suggestion_item['Item_Name']} has been dispensed\033[0m")

                yes_suggestion = ((change + insert_cash2) - suggestion_item['Price'])
                print(f"\nPlease get your remaining balance of AED", yes_suggestion)
       
        #The user said no to buying the suggested item
        elif suggestion == 'no':
            print("\n--------------------------------------------------")
            no_suggestion = (change + insert_cash2)
            print(f"\nPlease get your remaining balance of AED", no_suggestion)

        # Asking the user whether or not to repeat the purchase
        print(f"\n{BLUE}Do you want to buy anything else? \033[0m", end='')
        repeat = input()

        if repeat == 'no':
            print("\n--------------------------------------------------")
            print("\nThank you for using Munch Vending Machine. Have a great day!")
            sys.exit()  # Exit the program

# Starting the vending machine again because the user said yes to buying more
start()
