def solution():
    """Marnie opens a bag of chips and eats 5 of them to see if she likes them. She does, so she eats 5 more. The bag has 100 chips in it and starting on the second day she has them, Marnie eats 10 each day. How many days does it take for Marnie to eat the whole bag of chips?"""
    # Define the initial number of chips and the number Marnie eats on the first day
    initial_chips = 100
    eaten_first_day = 10

    # Calculate the number of days it takes for Marnie to eat the remaining chips
    remaining_chips = initial_chips - 10  # Marnie eats 10 on the first day
    days = 1  # already counting the first day
    while remaining_chips > 0:
        remaining_chips -= 10
        days += 1

    # Display the number of days
    result = days
    return result

print(solution())