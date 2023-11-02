def solution():
    """Lolita can drink 3 boxes of milk during weekdays. During Saturdays, she can drink twice the number of boxes of milk than on the weekdays, and during Sundays, she can drink thrice the number of boxes of milk than on the weekdays. How many boxes of milk does she drink per week?"""
    weekdays_milk = 3
    saturday_milk = 2 * weekdays_milk
    sunday_milk = 3 * weekdays_milk
    total_milk = (weekdays_milk * 5) + saturday_milk + sunday_milk
    result = total_milk
    return result

print(solution())