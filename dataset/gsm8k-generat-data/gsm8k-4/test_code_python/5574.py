def solution():
    """Mike wants to be the best goalkeeper on his soccer team. He practices for 3 hours every weekday, on Saturdays he practices for 5 hours, and he takes Sundays off. How many hours will he practice from now until the next game, if his team has a game in 3 weeks?"""
    # Define the number of practice days in a week
    practice_days = 6  # weekdays + Saturday

    # Define the number of hours practiced per day
    hours_per_day = 3

    # Calculate the total number of hours practiced per week
    weekly_hours = (practice_days * hours_per_day) + 5  # add Saturday's hours

    # Calculate the total number of hours practiced in 3 weeks
    total_hours = weekly_hours * 3

    # Return the result
    result = total_hours
    return result

print(solution())