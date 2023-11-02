def solution():
    """Erwin eats 2 chocolates on weekdays and 1 chocolate on weekends. He ate 24 chocolates in total. How many weeks did it take to finish all the chocolate?"""
    # Define the number of chocolates eaten on weekdays and weekends
    weekday_chocolates = 2
    weekend_chocolates = 1

    # Define the total number of chocolates eaten
    total_chocolates = 24

    # Define the number of weeks it takes to finish all the chocolates
    weeks = 0

    # Calculate the number of weeks it takes to eat all the chocolates
    while total_chocolates > 0:
        # Increment the week counter
        weeks += 1

        # Calculate the number of chocolates eaten during the current week
        chocolates_eaten = 0
        if weeks % 7 in [1, 2, 3, 4, 5]:
            chocolates_eaten = weekday_chocolates
        else:
            chocolates_eaten = weekend_chocolates

        # Subtract the number of chocolates eaten from the total
        total_chocolates -= chocolates_eaten

    # Return the number of weeks it took to finish all the chocolates
    result = weeks
    return result

print(solution())