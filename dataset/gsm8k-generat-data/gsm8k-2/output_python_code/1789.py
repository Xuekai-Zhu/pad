def solution():
    """The number of coronavirus cases in a certain country was 300 infections per day during the first wave. However, the number of cases increased by four times more per day as a new coronavirus variant started infecting people in a second wave. What was the total number of infections during the second wave in 2 weeks?"""
    first_wave_cases = 300
    second_wave_cases = 4 * first_wave_cases
    total_cases_in_two_weeks = 14 * 7 * second_wave_cases
    result = total_cases_in_two_weeks
    return result

print(solution())