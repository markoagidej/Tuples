# Task 1: Formatting Flight Itineraries

itinerary_list = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def print_itineraries(itineraries):
    count = 1
    for itinerary in itinerary_list:
        print(f"Itinerary {count}: {itinerary[0]} - From {itinerary[1]} to {itinerary[2]}")
        count += 1

print_itineraries(itinerary_list)