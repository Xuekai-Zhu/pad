def solution():
    """Mike wants to be the best goalkeeper on his soccer team. He practices for 3 hours every weekday, on Saturdays he practices for 5 hours, and he takes Sundays off. How many hours will he practice from now until the next game, if his team has a game in 3 weeks?"""
    # Define the number of days in a week and the number of weeks until the next game
    WEEKDAYS = 5
    WEEKS = 3

    # Calculate the total number of practice hours on weekdays
    weekday_hours = 3 * WEEKDAYS * WEEKS

    # Calculate the total number of practice hours on Saturdays
    saturday_hours = 5 * WEEKS

    # Calculate the total number of practice hours
    total_hours = weekday_hours + saturday_hours

    # Display the total number of practice hours
    result = total_hours
    return result

print(solution())