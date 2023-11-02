def solution():
    total_goal = 1000.0
    months = 12
    leftover_money = 100.0

    amount_to_save = (total_goal - leftover_money) / months
    result = amount_to_save
    return result

print(solution())