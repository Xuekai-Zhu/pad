def solution():
    """During vacation, Jimmy visits different beaches on an island, so he changes his place of lodging from time to time. The first 3 days he stays in a hostel, where he is charged $15 per night. The fourth and fifth days he stays in a cabin where he shares expenses with 2 of his friends, and they are charged $45 total per night. How much did Jimmy spend on lodging?"""
    hostel_cost = 15 * 3
    cabin_cost = 45 / 3 * 2
    total_cost = hostel_cost + cabin_cost
    result = total_cost
    return result

print(solution())