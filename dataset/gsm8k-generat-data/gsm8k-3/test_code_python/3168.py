def solution():
    """Michelle rode a taxi from her office to her home, which constitutes 4 miles. If the taxi charge per mile is $2.5, how much did pay Michelle pay in total for her ride?"""
    # Define the ride fee and the cost per mile
    RIDE_FEE = 2
    COST_PER_MILE = 2.5

    # Calculate the distance of the ride
    distance = 4

    # Calculate the cost of the ride
    cost = RIDE_FEE + (distance * COST_PER_MILE)

    # Display the total cost of the ride
    result = cost
    return result

print(solution())