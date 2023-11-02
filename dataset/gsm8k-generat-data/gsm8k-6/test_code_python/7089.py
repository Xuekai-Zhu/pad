def solution():
    # Calculate the total cost of renting the car for the two days
    monday_cost = 150 + (0.5 * 620)  # cost for Monday
    thursday_cost = 150 + (0.5 * 744)  # cost for Thursday
    total_cost = monday_cost + thursday_cost  # total cost for both days
    result = total_cost
    return result

print(solution())