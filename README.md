1. Tuple Mastery in Python
Objective:
The aim of this assignment is to deepen your understanding of tuples in Python, along with their interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, and string formatting. By completing this assignment, you will enhance your skills in data structuring, manipulation, and application of tuples in practical scenarios.

Task 1: Formatting Flight Itineraries
Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
2. Python Data Structure Challenges in Real-World Scenarios
Objective:
This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, and implementing error handling in practical situations.

Task 1: Library System Enhancement
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement:
You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
Add functionality to insert new books into library.
Ensure that adding a duplicate book is handled appropriately.
3. Python Loops and Tuples in Analytical Applications
Objective:

This assignment is designed to strengthen your expertise in using Python loops and tuples, particularly in data analysis and processing scenarios. By completing these tasks, you will gain practical experience in handling and analyzing data using these fundamental Python concepts.

Task 1: Stock Market Data Analysis
Enhance your skills in data manipulation and analysis using tuples and loops.

Problem Statement:
You have been provided with stock market data, where each data point is a tuple containing a company's stock symbol, the date, and the closing price. Your task is to analyze this data to find the average closing price of a specified stock over a given period.

Sample Data:

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]
Create a function to calculate the average closing price of a specific stock symbol over all dates.
Ensure your solution handles cases where the stock symbol does not exist in the data.
Task 2: Event Attendance Tracker
Apply loops and tuples to track and report on event attendance.

Problem Statement:
Your goal is to manage an attendance system for various events. Each attendee's data is stored as a tuple containing their name and the event they attended.

Develop a function to list all attendees of a specific event.
Implement a feature to count the number of attendees for each event.
Example Attendee Data:

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]
4. Mastering Tuple Packing and Unpacking in Python
Objective:
The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python. You will apply these techniques in various practical scenarios, enhancing your ability to work with flexible data structures and improve data handling efficiency.

Task 1: Customer Order Processing
Refine your skills in tuple unpacking by managing customer orders.

Problem Statement:
You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]
Write a function to iterate over the list of orders.
Unpack each tuple in the list and format the details for display.
Task 2: Sorting and Filtering Contact Information
Implement tuple packing and unpacking in sorting and filtering tasks.

Problem Statement:
You have a list of contacts, where each contact is represented as a tuple containing a name, email, and phone number. Your task is to:

Sort the contacts by name.
Filter and display contacts whose names start with a specific letter.
Sample Contact Data:

contacts = [
    ("Alice", "alice@email.com", "123-456-7890"),
    ("Bob", "bob@email.com", "234-567-8901"),
    # More contacts...
]
5. Advanced Tuple Techniques: Joining and Nesting in Python
Objective:
This assignment is designed to advance your understanding and application of joining and nesting tuples in Python. You will engage in tasks that require organizing and manipulating complex data structures, improving your problem-solving skills in handling multi-dimensional data.

Task 1: Product Catalog Merging
Utilize tuple joining to combine multiple product catalogs.

Problem Statement:
You are managing the product catalogs for an online store. Each catalog is a tuple of products, and each product is a tuple containing the product name and price. Merge multiple catalogs into a single tuple.

Write a function to join two or more product catalogs into one.
Display the combined catalog, ensuring that it maintains the order of products as they were in their original catalogs.
Example Catalogs:

catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))