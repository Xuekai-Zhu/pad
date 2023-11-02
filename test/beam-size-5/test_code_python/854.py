def solution():
    
    initial_infects = 10
    additional_infects_per_day = 6
    days = 3
    total_infected = initial_infects * additional_infects_per_day * days
    result = total_infected
    return result

print(solution())