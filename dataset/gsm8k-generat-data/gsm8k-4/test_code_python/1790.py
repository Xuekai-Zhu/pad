def solution():
    """The number of coronavirus cases in a certain country was 300 infections per day during the first wave. However, the number of cases increased by four times more per day as a new coronavirus variant started infecting people in a second wave. What was the total number of infections during the second wave in 2 weeks?"""
    # Calculate the number of infections per day during the second wave
    infections_per_day_second_wave = 300 * 4

    # Calculate the total number of infections during 2 weeks
    total_infections_second_wave = infections_per_day_second_wave * 14

    result = total_infections_second_wave
    return result

print(solution())