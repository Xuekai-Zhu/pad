def solution():
    days_to_save = 22  # Lilly has 22 days to save money
    saved_per_day = 2  # Lilly saves $2 each day
    flower_cost = 4  # Each flower costs $4

    # Calculate the total amount Lilly saves in 22 days
    total_saved = days_to_save * saved_per_day

    # Calculate the number of flowers Lilly can buy with her savings
    flowers_to_buy = total_saved // flower_cost
    result = flowers_to_buy
    return result

print(solution())