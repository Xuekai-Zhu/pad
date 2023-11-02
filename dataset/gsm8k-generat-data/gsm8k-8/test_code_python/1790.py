def solution():
    # Define the number of infections per day during the first wave
    first_wave_daily_cases = 300

    # Calculate the number of infections per day during the second wave
    second_wave_daily_cases = first_wave_daily_cases * 4

    # Calculate the total number of infections during the second wave in 2 weeks (14 days)
    second_wave_total_cases = second_wave_daily_cases * 14

    result = second_wave_total_cases
    return result

print(solution())