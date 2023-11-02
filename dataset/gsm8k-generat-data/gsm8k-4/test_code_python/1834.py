def solution():
    """During vacation, Jimmy visits different beaches on an island, so he changes his place of lodging from time to time. The first 3 days he stays in a hostel, where he is charged $15 per night. The fourth and fifth days he stays in a cabin where he shares expenses with 2 of his friends, and they are charged $45 total per night. How much did Jimmy spend on lodging?"""
    # Define the cost per night of the hostel
    hostel_cost = 15

    # Define the total number of nights spent in the hostel
    hostel_nights = 3

    # Define the total cost of staying in the hostel
    hostel_total = hostel_cost * hostel_nights

    # Define the total number of nights spent in the cabin
    cabin_nights = 2

    # Define the total cost of staying in the cabin
    cabin_total = 45

    # Calculate the cost per night of the cabin
    cabin_cost_per_night = cabin_total / 3

    # Calculate the total cost of staying in the cabin for Jimmy
    jimmy_cabin_total = cabin_cost_per_night * cabin_nights

    # Calculate the total lodging cost for Jimmy
    lodging_cost = hostel_total + jimmy_cabin_total

    # return the result
    result = lodging_cost
    return result

print(solution())