def solution():
    # Calculate the cost of hiring an assistant for 4 hours for one direction
    cost_one_direction = 10 * 4  # $10 per hour and 4 hours of crossing

    # Calculate the total cost of hiring an assistant for round trip
    total_cost = cost_one_direction * 2  # Tom needs to cross the lake back and forth
    result = total_cost
    return result

print(solution())