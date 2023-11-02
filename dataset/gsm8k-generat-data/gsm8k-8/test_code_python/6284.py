def solution():
    # Calculate the time it takes for Tara to reach the top floor
    tara_time = 20 * 8 + 19 * 3
    # Calculate the time it takes for Lola to reach the top floor
    lola_time = 20 * 10

    # Determine the slower time
    slower_time = max(tara_time, lola_time)
    result = slower_time
    return result

print(solution())