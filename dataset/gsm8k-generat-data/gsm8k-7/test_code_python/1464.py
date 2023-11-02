def solution():
    initial_production = 7000
    increase_factor = 3
    total_production = initial_production * increase_factor
    days_in_march = 31
    total_production_march = total_production * days_in_march
    result = total_production_march
    return result

print(solution())