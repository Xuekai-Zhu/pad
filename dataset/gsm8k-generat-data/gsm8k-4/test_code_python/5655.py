def solution():
    """Lolita can drink 3 boxes of milk during weekdays. During Saturdays, she can drink twice the number of boxes of milk than on the weekdays, and during Sundays, she can drink thrice the number of boxes of milk than on the weekdays. How many boxes of milk does she drink per week?"""
    # Define the number of boxes of milk Lolita drinks on weekdays
    weekdays_milk = 3

    # Define the number of boxes of milk Lolita drinks on Saturday
    saturday_milk = weekdays_milk * 2

    # Define the number of boxes of milk Lolita drinks on Sunday
    sunday_milk = weekdays_milk * 3

    # Calculate the total number of boxes of milk Lolita drinks per week
    total_milk = (weekdays_milk * 5) + saturday_milk + sunday_milk

    # return the result
    result = total_milk
    return result

print(solution())