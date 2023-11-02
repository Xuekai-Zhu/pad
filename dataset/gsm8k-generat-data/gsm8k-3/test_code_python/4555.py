def solution():
    """Maddy was given 40 chocolate eggs for Easter. She likes to eat two each day after school. If Maddy has two chocolate eggs after school each day, how many weeks will they last?"""
    # Define the number of chocolate eggs Maddy has and the number of eggs she eats per day
    eggs = 40
    eggs_per_day = 2

    # Calculate the number of days the eggs will last
    days = eggs // eggs_per_day

    # Calculate the number of weeks the eggs will last
    weeks = days // 7

    # Display the number of weeks
    result = weeks
    return result

print(solution())