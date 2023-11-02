def solution():
    cost_of_shirt = 3
    amount_saved = 1.5
    saving_per_week = 0.5

    # Calculate the remaining amount needed to buy the shirt
    remaining_amount = cost_of_shirt - amount_saved

    # Calculate the number of weeks Macey needs to save for the remaining amount
    num_weeks = remaining_amount / saving_per_week
    result = num_weeks
    return result

print(solution())