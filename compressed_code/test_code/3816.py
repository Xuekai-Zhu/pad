def solution():
    
    current_swans = 15
    doubling_time_years = 2
    years = 10
    doubling_times = years // doubling_time_years
    total_swans = current_swans * (2 ** doubling_times)
    result = total_swans
    return result

print(solution())