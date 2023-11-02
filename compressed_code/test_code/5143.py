def solution():
    
    meat_cost = 20 * 5
    fruit_veg_cost = 15 * 4
    bread_cost = 60 * 1.5
    janitor_pay = 10 * 1.5 * 10
    total_cost = meat_cost + fruit_veg_cost + bread_cost + janitor_pay
    hours_worked = total_cost / 8
    result = hours_worked
    return result

print(solution())