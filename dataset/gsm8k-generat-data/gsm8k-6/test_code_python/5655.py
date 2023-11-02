def solution():
    # Calculate the total number of milk boxes Lolita drinks per week
    weekday_milk = 3 * 5  # Lolita drinks 3 boxes of milk during weekdays for 5 days
    saturday_milk = 3 * 2  # Lolita drinks twice the number of boxes on Saturdays compared to weekdays
    sunday_milk = 3 * 3  # Lolita drinks thrice the number of boxes on Sundays compared to weekdays
    total_milk = weekday_milk + saturday_milk + sunday_milk
    result = total_milk
    return result

print(solution())