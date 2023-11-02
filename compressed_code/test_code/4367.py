def solution():
    
    weekdays_milk = 3
    saturday_milk = 2 * weekdays_milk
    sunday_milk = 3 * weekdays_milk
    total_milk = (weekdays_milk * 5) + saturday_milk + sunday_milk
    result = total_milk
    return result

print(solution())