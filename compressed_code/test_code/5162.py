def solution():
    
    craig_day1 = 40
    craig_day2 = 40 + 60
    heather_day1 = 4 * craig_day1
    heather_day2 = craig_day2 - 20
    total_pizzas = craig_day1 + craig_day2 + heather_day1 + heather_day2
    result = total_pizzas
    return result

print(solution())