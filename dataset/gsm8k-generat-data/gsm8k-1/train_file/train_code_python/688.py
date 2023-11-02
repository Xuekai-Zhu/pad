def solution():
    """Trevor needs to go downtown for a restaurant date. An Uber ride downtown costs $3 more than a Lyft ride. A Lyft ride costs $4 more than a taxi ride. The Uber ride costs $22. If Trevor takes a taxi downtown and tips the taxi driver 20% of the original cost of the ride, what is the total cost of the ride downtown?"""
    taxi_cost = 0
    lyft_cost = taxi_cost + 4
    uber_cost = lyft_cost + 3

    tip_percent = 20

    taxi_tip = taxi_cost * (tip_percent / 100)
    taxi_total_cost = taxi_cost + taxi_tip

    result = taxi_total_cost

    return result

print(solution())