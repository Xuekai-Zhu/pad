def solution():
    initial_cows = 39  # The man initially had 39 cows
    cows_dead = 25  # Last year, 25 cows died
    cows_sold = 6  # Last year, the man sold 6 cows
    current_cows = initial_cows - cows_dead - cows_sold  # Calculate the current number of cows

    current_cows += 24  # This year, the number of cows increased by 24
    current_cows += 43  # The man bought 43 more cows
    current_cows += 8  # His friend gave him 8 cows as a gift

    result = current_cows
    return result

print(solution())