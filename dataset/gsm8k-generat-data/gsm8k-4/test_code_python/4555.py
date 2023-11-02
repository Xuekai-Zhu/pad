def solution():
    """Maddy was given 40 chocolate eggs for Easter. She likes to eat two each day after school. If Maddy has two chocolate eggs after school each day, how many weeks will they last?"""
    # Define the number of chocolate eggs Maddy has
    chocolate_eggs = 40

    # Define the number of chocolate eggs Maddy eats each day
    eggs_per_day = 2

    # Calculate the number of days the chocolate eggs will last
    days = chocolate_eggs / eggs_per_day

    # Calculate the number of weeks the chocolate eggs will last
    weeks = days / 7

    # Round up to the nearest whole week
    weeks = round(weeks + 0.5)

    # Return the result
    result = weeks
    return result

print(solution())