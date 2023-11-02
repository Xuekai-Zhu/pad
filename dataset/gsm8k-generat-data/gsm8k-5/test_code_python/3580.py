def solution():
    total_seedlings_planted = 1200  # The total number of seedlings planted on the first and second day
    first_day_seedlings = 200  # The number of seedlings planted on the first day
    second_day_seedlings = 2 * first_day_seedlings  # Twice the number of seedlings planted on the first day
    remaining_seedlings = total_seedlings_planted - first_day_seedlings - second_day_seedlings  # The number of seedlings planted by Remi's father

    result = remaining_seedlings
    return result

print(solution())