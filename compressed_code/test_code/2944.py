def solution():
    
    start_age = 18
    chief_time = 8
    master_chief_time = 1.25 * chief_time
    total_time = chief_time + master_chief_time + 10
    retired_age = start_age + total_time
    result = retired_age
    return result

print(solution())