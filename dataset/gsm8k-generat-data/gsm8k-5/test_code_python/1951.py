def solution():
    starting_chips = 100  # There are 100 chips in the bag
    marnie_likes_chips = 10  # Marnie eats 10 chips per day after the first day
    days_until_finished = 1  # It takes Marnie 1 day to eat the first 10 chips

    # Marnie eats 10 chips per day, so subtracting the first 10 she ate, we get the remaining chips
    remaining_chips = starting_chips - 10
    while remaining_chips > 0:
        remaining_chips -= marnie_likes_chips
        days_until_finished += 1

    result = days_until_finished
    return result

print(solution())