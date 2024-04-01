# Task 1: Stock Market Data Analysis

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def average_closinp_price_of(symbol):
    price_total = 0
    days = 0

    for stock in stock_data:
        if stock[0] == symbol:
            price_total += stock[2]
            days += 1

    if days != 0:
        print(f"Average price of {symbol} over {days} days: {price_total/days}")
    else:
        print("That stock was not in this list.")



#average_closinp_price_of(input("Enter the symbol of the stock you wish to find the average closing price for: ").upper())


# Task 2: Event Attendance Tracker

attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]

def list_attendees(event):
    attendence_list = []
    for person in attendees:
        if person[1].lower() == event.lower():
            attendence_list.append(person[0])

    if attendence_list:
        print(f"List of attendees for {event}")
        for person in attendence_list:
            print(person)
    else:
        print(f"No attendees reported for {event}.")

def count_attendees_at_events():
    event_list = {}
    for person in attendees:
        if person[1] not in event_list:
            event_list[person[1]] = 1
        else:
            event_list[person[1]] += 1

    for event, count in event_list.items():
        print(f"{event}: {count} attendees")


list_attendees(input("Which event would you like to see a list of attendees for: "))
count_attendees_at_events()