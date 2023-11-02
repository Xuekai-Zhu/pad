def solution():
    required_ounces = 80
    can_size = 8
    can_cost = 0.5

    # Calculate the number of cans Peter needs
    num_cans = required_ounces / can_size

    # Calculate the total cost of all cans of soda that Peter will buy
    total_cost = num_cans * can_cost
    result = total_cost
    return result

print(solution())