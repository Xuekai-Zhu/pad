def solution():
    first_wave_cases_per_day = 300
    second_wave_cases_multiplier = 4
    days_in_two_weeks = 14

    # Calculate the total number of cases during the second wave
    second_wave_cases_per_day = first_wave_cases_per_day * second_wave_cases_multiplier
    total_cases_second_wave = second_wave_cases_per_day * days_in_two_weeks
    result = total_cases_second_wave
    return result

print(solution())