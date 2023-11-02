def solution():
    # Calculate the cost of one chip
    cost_per_chip = 2/24  # the bag costs $2 and has 24 chips

    # Calculate the cost of 480 calories worth of chips
    total_chips = 480/10  # each chip is 10 calories
    total_cost = total_chips * cost_per_chip
    result = total_cost
    return result

print(solution())