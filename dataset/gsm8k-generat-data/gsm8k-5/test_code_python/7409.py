def solution():
    # Calculate the total number of squares of toilet paper Bill has
    total_squares = 1000 * 300

    # Calculate the number of squares Bill uses per day
    squares_per_day = 5 * 3

    # Calculate the number of days Bill's toilet paper supply will last
    days_supply = total_squares / squares_per_day
    result = days_supply
    return result

print(solution())