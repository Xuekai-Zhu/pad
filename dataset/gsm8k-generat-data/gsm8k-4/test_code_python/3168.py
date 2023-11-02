def solution():
    """As soon as you enter the taxi, you pay a ride fee of $2. Michelle rode a taxi from her office to her home, which constitutes 4 miles. If the taxi charge per mile is $2.5, how much did pay Michelle pay in total for her ride?"""
    # Define the ride fee and the cost per mile
    ride_fee = 2
    cost_per_mile = 2.5

    # Define the distance and calculate the total cost
    distance = 4
    total_cost = ride_fee + (distance * cost_per_mile)

    result = total_cost
    return result

print(solution())