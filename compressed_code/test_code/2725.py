def solution():
    
    total_goal = 1000
    leftover_money = 100
    months_to_save = 12
    amount_to_save_per_month = (total_goal - leftover_money) / months_to_save
    result = amount_to_save_per_month
    return result

print(solution())