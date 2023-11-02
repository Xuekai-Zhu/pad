def solution():
    """Gary buys 4 chickens. After two years, he has 8 times as many chickens as he started with. If each chicken lays 6 eggs a day, how many eggs does Gary currently collect every week?"""
    # Define the initial number of chickens and the number of years passed
    initial_chickens = 4
    years_passed = 2

    # Calculate the current number of chickens
    current_chickens = initial_chickens * 8

    # Calculate the current number of eggs collected per day
    eggs_per_day = current_chickens * 6

    # Calculate the current number of eggs collected per week
    eggs_per_week = eggs_per_day * 7

    # Display the current number of eggs collected per week
    result = eggs_per_week
    return result

print(solution())