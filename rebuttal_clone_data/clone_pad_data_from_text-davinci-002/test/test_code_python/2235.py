def solution():
    initial_clean_and_jerk = 80
    initial_snatch = 50
    new_clean_and_jerk = initial_clean_and_jerk * 2
    new_snatch = initial_snatch * 1.8
    total_lifting_capacity = new_clean_and_jerk + new_snatch
    result = total_lifting_capacity
    return result

print(solution())