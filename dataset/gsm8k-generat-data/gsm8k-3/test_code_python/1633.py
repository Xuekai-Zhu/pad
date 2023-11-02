def solution():
    """Erwin eats 2 chocolates on weekdays and 1 chocolate on weekends. He ate 24 chocolates in total. How many weeks did it take to finish all the chocolate?"""
    # Define the number of chocolates he eats on weekdays and weekends
    WEEKDAY_CHOCOLATES = 2
    WEEKEND_CHOCOLATES = 1

    # Define the total number of chocolates he ate
    total_chocolates = 24

    # Calculate the number of weekdays and weekends
    num_weekdays = 5
    num_weekends = 2

    # Calculate the total number of chocolates he can eat in one week
    chocolates_per_week = (WEEKDAY_CHOCOLATES * num_weekdays) + (WEEKEND_CHOCOLATES * num_weekends)

    # Calculate the number of weeks it took Erwin to finish all the chocolates
    num_weeks = total_chocolates // chocolates_per_week

    # Display the number of weeks
    result = num_weeks
    return result

print(solution())