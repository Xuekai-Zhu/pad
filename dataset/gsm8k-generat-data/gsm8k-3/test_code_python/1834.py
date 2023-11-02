def solution():
    """During vacation, Jimmy visits different beaches on an island, so he changes his place of lodging from time to time. 
    The first 3 days he stays in a hostel, where he is charged $15 per night. 
    The fourth and fifth days he stays in a cabin where he shares expenses with 2 of his friends, and they are charged $45 total per night. 
    How much did Jimmy spend on lodging?"""
    
    # Calculate the cost of the hostel stay
    hostel_cost = 15 * 3
    
    # Calculate the cost of the cabin stay per night
    cabin_cost_per_night = 45 / 3
    
    # Calculate the cost of Jimmy's stay in the cabin
    cabin_cost = cabin_cost_per_night * 2
    
    # Calculate the total lodging cost
    total_cost = hostel_cost + cabin_cost
    
    # Return the total lodging cost
    result = total_cost
    return result

print(solution())