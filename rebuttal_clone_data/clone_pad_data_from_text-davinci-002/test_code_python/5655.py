def solution():
    weekday_milk = 3
    saturday_milk = weekday_milk * 2
    sunday_milk = weekday_milk * 3
    total_milk = weekday_milk * 5 + saturday_milk + sunday_milk
    result = total_milk
    return result

print(solution())