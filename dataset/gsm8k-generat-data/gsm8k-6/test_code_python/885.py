def solution():
    # Calculate the total cost for making the shoes
    cost_for_work = 75 * 8  # $75 an hour for 8 hours
    total_cost = 250 + cost_for_work  # $250 for making the mold + cost for work
    discounted_cost = total_cost * 0.8  # 80% of the total cost since it's the first pair of shoes

    result = discounted_cost
    return result

print(solution())