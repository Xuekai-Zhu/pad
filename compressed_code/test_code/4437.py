def solution():
    
    old_plan_price = 150
    increase_percent = 30
    new_plan_price = old_plan_price + (old_plan_price * increase_percent / 100)
    result = new_plan_price
    return result

print(solution())