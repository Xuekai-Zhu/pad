def solution():
    weekday_milk = 3
    saturday_milk = 2 * weekday_milk
    sunday_milk = 3 * weekday_milk

    total_milk = weekday_milk * 5 + saturday_milk + sunday_milk
    result = total_milk
    return result

print(solution())