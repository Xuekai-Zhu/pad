def solution():
    task_rate = 2
    bonus_task_num = 10
    bonus_amount = 6
    total_tasks = 30
    
    # Calculate the number of times Maurice will receive a bonus
    bonus_count = total_tasks // bonus_task_num
    
    # Calculate the total bonus amount Maurice will receive
    total_bonus = bonus_count * bonus_amount
    
    # Calculate the total amount earned for all tasks, including bonuses
    total_earned = (total_tasks * task_rate) + total_bonus
    
    result = total_earned
    return result

print(solution())