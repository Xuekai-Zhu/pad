def solution():
    # Calculate the time it takes for Tara to reach the top floor
    time_Tara = 19 * 8 + 20 * 3  # she stops for 3 seconds on every floor
    # Calculate the time it takes for Lola to reach the top floor
    time_Lola = 10 * 20
    # Find the slower one of Lola and Tara
    slower_time = max(time_Tara, time_Lola)
    result = slower_time
    return result

print(solution())