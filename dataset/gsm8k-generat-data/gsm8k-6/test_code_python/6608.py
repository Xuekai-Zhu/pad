def solution():
    # calculate the cost of replacing all the bikes
    bike_cost = 700 * 10 * 20

    # calculate the cost of replacing all the treadmills (50% more expensive than bikes)
    treadmill_cost = 1.5 * 700 * 5 * 20 

    # calculate the cost of replacing all the elliptical machines (twice as expensive as treadmills)
    elliptical_cost = 2 * 1.5 * 700 * 5 * 20 

    # calculate the total cost of replacing everything
    total_cost = bike_cost + treadmill_cost + elliptical_cost
    result = total_cost
    return result

print(solution())