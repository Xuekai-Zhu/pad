def solution():
    """Lolita can drink 3 boxes of milk during weekdays. During Saturdays, she can drink twice the number of boxes of milk
    than on the weekdays, and during Sundays, she can drink thrice the number of boxes of milk than on the weekdays. How
    many boxes of milk does she drink per week?"""
    weekday_milk = 3
    saturday_milk = 2 * weekday_milk
    sunday_milk = 3 * weekday_milk
    total_milk = weekday_milk * 5 + saturday_milk + sunday_milk
    result = total_milk
    return result

print(solution())