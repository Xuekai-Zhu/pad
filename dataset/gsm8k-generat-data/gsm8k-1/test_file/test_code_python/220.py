def solution():
    """Carlos and Benji are at the beach. Carlos rents a canoe for $30 an hour and Benji rents a banana boat raft for $18 an hour. If Carlos uses the boat for 3 hours and Benji uses the raft for 5 hours, how much will they pay for their rentals, altogether?"""
    canoe_rental_rate = 30
    banana_boat_rental_rate = 18
    canoe_hours = 3
    banana_boat_hours = 5
    total_cost = (canoe_rental_rate * canoe_hours) + (banana_boat_rental_rate * banana_boat_hours)
    result = total_cost
    return result

print(solution())