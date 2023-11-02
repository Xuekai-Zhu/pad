def solution():
    """The fall semester lasts 15 weeks. During the weekdays, Paris studies 3 hours a day for her classes. On the weekends, she spends 4 hours studying on Saturday and 5 hours studying on Sunday. How much time does Paris study during the semester?"""
    # Define the number of weekdays and weekends in the semester
    num_weekdays = 5 * 15
    num_weekends = 2 * 15

    # Define the number of hours Paris studies per day on weekdays and weekends
    weekday_hours = 3
    weekend_hours = 4 + 5

    # Calculate the total number of hours Paris studies during the semester
    total_hours = num_weekdays * weekday_hours + num_weekends * weekend_hours

    # Return the result
    result = total_hours
    return result

print(solution())