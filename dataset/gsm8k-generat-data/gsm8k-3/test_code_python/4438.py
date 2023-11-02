def solution():
    """The fall semester lasts 15 weeks.  During the weekdays, Paris studies 3 hours a day for her classes.  On the weekends, she spends 4 hours studying on Saturday and 5 hours studying on Sunday.  How much time does Paris study during the semester?"""
    # Define the number of weeks in the fall semester
    WEEKS = 15

    # Calculate the total number of hours Paris studies during the weekdays
    weekday_hours = 3 * 5 * WEEKS

    # Calculate the total number of hours Paris studies on the weekends
    weekend_hours = (4 + 5) * 2 * WEEKS

    # Calculate the total number of hours Paris studies during the semester
    total_hours = weekday_hours + weekend_hours

    # Display the total number of hours Paris studies
    result = total_hours
    return result

print(solution())