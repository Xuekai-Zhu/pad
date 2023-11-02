def solution():
    """Gina's snake eats one mouse every 4 weeks. How many mice will it eat in a decade?"""
    # Define the number of weeks in a decade
    WEEKS_IN_DECADE = 10 * 52

    # Calculate the number of mice the snake will eat in a decade
    mice_eaten = WEEKS_IN_DECADE // 4

    # Display the number of mice eaten
    result = mice_eaten
    return result

print(solution())