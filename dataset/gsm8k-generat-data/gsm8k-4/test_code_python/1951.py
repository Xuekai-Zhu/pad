def solution():
    """Marnie opens a bag of chips and eats 5 of them to see if she likes them. She does, so she eats 5 more.
    The bag has 100 chips in it and starting on the second day she has them, Marnie eats 10 each day.
    How many days does it take for Marnie to eat the whole bag of chips?"""
    
    # Define the initial number of chips in the bag
    chips_remaining = 100

    # Eat 5 chips to see if she likes them
    chips_remaining -= 5

    # Eat 5 more chips
    chips_remaining -= 5

    # Initialize the day counter
    days = 1

    # Keep eating chips each day until the bag is empty
    while chips_remaining > 0:
        chips_remaining -= 10
        days += 1
    
    # Display the number of days it takes to eat the whole bag
    result = days
    return result

print(solution())