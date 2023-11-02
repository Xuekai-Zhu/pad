def solution():
    
    time_to_learn_rules = 2
    time_to_get_proficient = 49 * time_to_learn_rules
    time_to_become_master = 100 * (time_to_learn_rules + time_to_get_proficient)
    total_time = time_to_learn_rules + time_to_get_proficient + time_to_become_master
    result = total_time
    return result

print(solution())