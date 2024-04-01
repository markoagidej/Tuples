# Task 1: Customer Order Processing

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

def readable_orders(order_list):
    for order in order_list:
        name, item, quantity = order
        print(f"Customer {name} placed and order for the item: {item}, with a quantity of {quantity}.")

readable_orders(orders)

# Task 2: Sorting and Filtering Contact Information

contacts = [
    ("Bob", "bob@email.com", "234-567-8901"),
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Zoro", "bob@email.com", "234-567-8901"),
    ("Candice", "alice@email.com", "123-456-7890"),
    # More contacts...
]

def sort_contacts(contact_list):
    sorted_list = sorted(contact_list)
    for contact in sorted_list:
        print(contact)

def filter_contacts(filter_letter):
    filter_list = []
    if filter_letter:
        if len(filter_letter) == 1:
            for person in contacts:
                if person[0][0] == filter_letter:
                    filter_list.append(person)
            
            print(f"Dispalying all contacts whos name starts with {filter_letter}:")
            for contact in filter_list:
                print(contact)
        else:
            print("Cannot input more than a single letter to filter!")
    else:
        print("Must input a single letter to filter!")

sort_contacts(contacts)
#filter_contacts(input("Enter the first letter of contacts you would like to see: ").upper())