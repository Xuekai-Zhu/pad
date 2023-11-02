def solution():
    """Marnie opens a bag of chips and eats 5 of them to see if she likes them. She does, so she eats 5 more. The bag has 100 chips in it and starting on the second day she has them, Marnie eats 10 each day. How many days does it take for Marnie to eat the whole bag of chips?"""
    starting_chips = 100
    eaten_on_first_day = 10
    remaining_chips = starting_chips - 10
    days = 0
    while remaining_chips > 0:
        days += 1
        if days == 1:
            remaining_chips -= 5
            remaining_chips -= 5
        else:
            remaining_chips -= 10
    result = days
    return result

print(solution())