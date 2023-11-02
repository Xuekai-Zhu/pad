def solution():
    """Trevor needs to go downtown for a restaurant date. An Uber ride downtown costs $3 more than a Lyft ride. A Lyft ride costs $4 more than a taxi ride. The Uber ride costs $22. If Trevor takes a taxi downtown and tips the taxi driver 20% of the original cost of the ride, what is the total cost of the ride downtown?"""
    uber_cost = 22
    lyft_cost = uber_cost - 3
    taxi_cost = lyft_cost - 4
    tip_percentage = 0.2
    taxi_tip = taxi_cost * tip_percentage
    total_cost = taxi_cost + taxi_tip
    result = total_cost
    return result

print(solution())