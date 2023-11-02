def solution():
    
    first_day = 10
    increase_per_day = 4
    days = 5
    total_money = first_day
    for i in range(1, days):
        total_money += (first_day + increase_per_day * i)
    result = total_money
    return result

print(solution())