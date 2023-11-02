def solution():
     old_plan = 150
     percent_increase = 30
     increase_amount = old_plan * (percent_increase / 100)
     new_plan = old_plan + increase_amount
     result = new_plan
     return result

print(solution())