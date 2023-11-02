def solution():
    
    assignment_time = 10
    one_key_time = 3
    remaining_keys = 14
    total_cleaning_time = one_key_time * remaining_keys
    total_time = total_cleaning_time + assignment_time
    result = total_time
    return result

print(solution())