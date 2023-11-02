def solution():
    taxi_cost = (22-3) - 4  # cost of taxi ride, taking into account prices of Uber and Lyft rides
    tip = taxi_cost * 0.2  # 20% tip on the original cost of the ride
    total_cost = taxi_cost + tip
    result = total_cost
    return result

print(solution())