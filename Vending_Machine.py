txt = 'Welcome to Munch Vending Machine'
print(txt.center(185))

print("""
                                                                                ░█▀▄▀█ ░█▀▀▀ ░█▄─░█ ░█─░█ 
                                                                                ░█░█░█ ░█▀▀▀ ░█░█░█ ░█─░█ 
                                                                                ░█──░█ ░█▄▄▄ ░█──▀█ ─▀▄▄▀
      
      """)

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

# Vending Machine Label
def print_section_title(title):
    line = "-" * 68
    formatted_title = f"{title.center(185)}\n{line.center(184)}"  #line under item label ex. drinks
    print(formatted_title)

print_section_title("𝑫 𝑹 𝑰 𝑵 𝑲 𝑺​​​​​")
print_table(A_items)

print_section_title("𝑪 𝑯 𝑰 𝑷 𝑺")
print_table(B_items)

print_section_title("𝑺 𝑾 𝑬 𝑬 𝑻 𝑺")
print_table(C_items)

while True:
    PURPLE = '\033[95m'
    input_user = input(f"\nEnter the code of the product you want to buy (or 'exit' to end): ")
    
    if input_user == 'exit':
        print("""-------------------------------------------------------------------- 
              Thank you for using Munch Vending Machine. Have a great day!""")
        break

    selected_item = None
    for item in A_items + B_items + C_items:
        if item['Code'] == input_user:
            selected_item = item
            break

    if selected_item['Stock'] == 0:
        print("""-------------------------------------------------------------------------
              
Sorry, this item is out of stock. Please choose another product.
              """)
        continue
    print ("-------------------------------------------------------------------------")
    print(f"\nYou have selected: {selected_item['Item_Name']}")
    print(f"Price: {selected_item['Price']}")
    print(f"Stock: {selected_item['Stock']}")
    break

insert_cash = float(input(f"\nPlease insert {selected_item['Price']}: "))

import sys

change = insert_cash - selected_item['Price']
print("\n-------------------------------------------------------------------------")
print("\n" + selected_item['Item_Name'] + " has been dispensed")
print ("\nYour remaining balance is AED", change)

input("\nPress Enter...")

# Suggestions in each items

if selected_item['Item_Name'] == "Coke":
    suggestion_item = B_items[0]
    print(f"""
--------------------------------------------------

{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
    print(f"This item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

elif selected_item['Item_Name'] == "Milk":
    suggestion_item = B_items[4]
    print(f"""
--------------------------------------------------
          
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
    print(f"This item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

elif selected_item['Item_Name'] == "Apple Juice":
    suggestion_item = B_items[1]
    print(f"""
--------------------------------------------------
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
    print(f"This item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

elif selected_item['Item_Name'] == "Coconut Juice":
    suggestion_item = B_items[3]
    print(f"""
--------------------------------------------------
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
    print(f"This item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

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
    print(f"This item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

elif selected_item['Item_Name'] == "Cheetos":
    suggestion_item = A_items[1]
    print(f"""
--------------------------------------------------
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
    print(f"This item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

elif selected_item['Item_Name'] == "Doritos":
    suggestion_item = A_items[4]
    print(f"""
--------------------------------------------------
{selected_item['Item_Name']} goes best with {suggestion_item['Item_Name']}!""")
    print(f"This item is {suggestion_item['Price']} AED and has {suggestion_item['Stock']} in stock")

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

if change < suggestion_item['Price']: # If the balamce money is not enough
    insert_cash2 = float(input(f"\nYou need to insert {suggestion_item['Price'] - change} AED more: "))
    if change + insert_cash2 >= suggestion_item['Price']:
        print("--------------------------------------------------")
        print(f"\n{suggestion_item['Item_Name']} has been dispensed")
        print(f"\nYour remaining balance is AED {(change + insert_cash2) - suggestion_item['Price']}")
else: 
    print("--------------------------------------------------")
    print(f"\n{suggestion_item['Item_Name']} has been dispensed")
    print(f"\nYour remaining balance is AED {(change + insert_cash2) - suggestion_item['Price']}")

Yes_No = input("\nDo you want to buy anything else? ")

if Yes_No == 'no':
    print("--------------------------------------------------")
    print(f"\nHere is your {(change + insert_cash2) - suggestion_item['Price']} AED change")

    print("\nThank you for using Munch Vending Machine. Have a great day!")
    sys.exit()  # Exit the program

elif Yes_No == 'yes':
    input_user2 = input("Enter the Code of the item you wish to buy: ")
