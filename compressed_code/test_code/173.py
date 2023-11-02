def solution():
    
    total_money = (7*1) + (4*5) + (2*10) + (1*20)
    peanuts_cost = 3
    total_spent = total_money - 4
    total_pounds = total_spent / peanuts_cost
    pounds_per_day = total_pounds / 7
    result = pounds_per_day
    return result

print(solution())