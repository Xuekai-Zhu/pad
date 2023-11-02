def solution():
    # Calculate the total number of infections during the second wave in 2 weeks
    first_wave_cases = 300  # number of cases in the first wave
    second_wave_cases = first_wave_cases * 4  # number of cases during the second wave
    total_cases = (14 * 7/1) * second_wave_cases  # total number of infections during 2 weeks
    result = total_cases
    return result

print(solution())