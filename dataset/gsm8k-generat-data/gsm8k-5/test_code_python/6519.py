def solution():
    snails_eaten = 3  # On the first day, a snail kite ate 3 snails
    for day in range(2, 6):  # Loop through the next 4 days
        snails_eaten += snails_eaten + 2  # Add 2 more snails than the day before
    total_snails_eaten = snails_eaten  # The total number of snails eaten is the sum of all 5 days
    result = total_snails_eaten
    return result

print(solution())