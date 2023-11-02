def solution():
    """During vacation, Jimmy visits different beaches on an island, so he changes his place of lodging from time to time. The first 3 days he stays in a hostel, where he is charged $15 per night. The fourth and fifth days he stays in a cabin where he shares expenses with 2 of his friends, and they are charged $45 total per night. How much did Jimmy spend on lodging?"""

    hostel_nights = 3
    hostel_price = 15
    cabin_nights = 2
    cabin_price = 45 / 3  # shared with 2 friends
    total_lodging_cost = (hostel_nights * hostel_price) + (cabin_nights * cabin_price)
    result = total_lodging_cost
    return result

print(solution())