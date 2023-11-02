def solution():
    first_wave_cases = 300  # Number of cases per day during the first wave
    second_wave_cases = 4 * first_wave_cases  # Number of cases per day during the second wave

    # Total number of infections during the second wave in 2 weeks (14 days)
    total_cases_second_wave = second_wave_cases * 14

    result = total_cases_second_wave
    return result

print(solution())