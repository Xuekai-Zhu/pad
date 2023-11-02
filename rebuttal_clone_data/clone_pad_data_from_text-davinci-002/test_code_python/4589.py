def solution():
    time_to_clean_one_egg = 15
    time_to_clean_one_roll = 30
    total_time_to_clean_eggs = time_to_clean_one_egg * 60
    total_time_to_clean_rolls = time_to_clean_one_roll * 7
    total_time = total_time_to_clean_eggs + total_time_to_clean_rolls
    result = total_time
    return result

print(solution())