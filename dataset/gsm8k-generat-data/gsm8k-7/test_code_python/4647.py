def solution():
    money_per_week = 15
    num_weeks = 60
    num_repetitions = 5

    # Calculate the total amount of money saved during one cycle
    total_money_per_cycle = money_per_week * num_weeks

    # Calculate the total amount of money saved over all cycles
    total_money_saved = total_money_per_cycle * num_repetitions

    result = total_money_saved
    return result

print(solution())