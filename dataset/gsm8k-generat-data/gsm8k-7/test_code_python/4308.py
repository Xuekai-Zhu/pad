def solution():
    cost_per_dozen = 5
    total_cost = 15

    # Calculate the total number of dozens of rolls that John bought
    total_dozen = total_cost / cost_per_dozen

    # Calculate the total number of rolls
    total_rolls = total_dozen * 12
    result = total_rolls
    return result

print(solution())