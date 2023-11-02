def solution():
    # Calculate the total cost of the 28 toys
    cost_of_toys = 28 * 10

    # Calculate the total cost of all the toys
    total_cost = cost_of_toys + (20 * x) # Assuming each teddy bear costs x dollars

    # Calculate the cost of one teddy bear
    cost_per_bear = (580 - total_cost) / 20
    result = cost_per_bear
    return result

print(solution())