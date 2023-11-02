def solution():
    time_to_learn_rules = 2  # It takes James 2 hours to learn the rules
    time_to_get_proficient = 49 * time_to_learn_rules  # It takes James 49 times the time to learn the rules to get proficient
    time_to_become_master = 100 * (time_to_learn_rules + time_to_get_proficient)  # James spends 100 times as much time to becoming a master as the combined time to get proficient

    # Calculate the total time James spent
    total_time = time_to_learn_rules + time_to_get_proficient + time_to_become_master
    result = total_time
    return result

print(solution())