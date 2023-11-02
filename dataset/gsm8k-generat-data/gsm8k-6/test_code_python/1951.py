def solution():
    # Calculate the total number of days it takes for Marnie to eat the whole bag of chips
    remaining_chips = 100 - 10  # Marnie eats 5 + 5 = 10 chips on the first day, so the remaining chips are 100 - 10 = 90
    days = 1  # start counting from the second day
    while remaining_chips > 0:
        remaining_chips -= 10  # Marnie eats 10 chips each day
        days += 1
    result = days
    return result

print(solution())