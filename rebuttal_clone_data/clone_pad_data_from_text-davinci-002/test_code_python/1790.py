def solution():
    initial_cases = 300
    variant_multiplier = 4
    total_cases = initial_cases * variant_multiplier
    days_in_second_wave = 14
    total_infections = total_cases * days_in_second_wave
    result = total_infections
    return result

print(solution())