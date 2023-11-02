def solution():
    
    sets = 3
    pushups_per_set = 15
    last_set_pushups = pushups_per_set - 5
    total_pushups = (pushups_per_set * (sets - 1)) + last_set_pushups
    result = total_pushups
    return result

print(solution())