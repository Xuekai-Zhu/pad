def solution():
    """Marnie opens a bag of chips and eats 5 of them to see if she likes them. She does, so she eats 5 more. The bag has 100 chips in it and starting on the second day she has them, Marnie eats 10 each day. How many days does it take for Marnie to eat the whole bag of chips?"""
    initial_chips_eaten = 10
    remaining_chips = 100 - initial_chips_eaten
    days_to_finish_remaining_chips = remaining_chips / 10
    total_days = 1 + days_to_finish_remaining_chips
    result = total_days
    return result

print(solution())