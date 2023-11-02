def solution():
     tasks_finished = 30
     money_per_task = 2
     bonus_threshold = 10
     bonus_amount = 6
    
     total_money = tasks_finished * money_per_task
     if tasks_finished >= bonus_threshold:
         total_money += bonus_amount
    
     result = total_money
     return result

print(solution())