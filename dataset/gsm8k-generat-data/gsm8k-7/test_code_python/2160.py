def solution():
    pants_cost = 50
    shirt_cost_multiplier = 1.6  # 60% more than pants

    # Calculate the cost of John's shirt
    shirt_cost = pants_cost * shirt_cost_multiplier

    # Calculate the total cost of John's outfit
    total_outfit_cost = pants_cost + shirt_cost
    result = total_outfit_cost
    return result

print(solution())