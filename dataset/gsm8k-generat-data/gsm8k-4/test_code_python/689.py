def solution():
    """Trevor needs to go downtown for a restaurant date. An Uber ride downtown costs $3 more than a Lyft ride. A Lyft ride costs $4 more than a taxi ride. The Uber ride costs $22. If Trevor takes a taxi downtown and tips the taxi driver 20% of the original cost of the ride, what is the total cost of the ride downtown?"""
    # Define the cost of the Uber ride
    uber_cost = 22

    # Calculate the cost of the Lyft ride
    lyft_cost = uber_cost - 3

    # Calculate the cost of the taxi ride
    taxi_cost = lyft_cost - 4

    # Calculate the tip amount for the taxi ride
    taxi_tip = taxi_cost * 0.2

    # Calculate the total cost of the taxi ride including tip
    total_cost = taxi_cost + taxi_tip

    result = total_cost
    return result

print(solution())