def solution():
    total_time = 9  # The whole process takes 9 hours
    dyeing_time = total_time * 2 / 3  # Dyeing takes twice as long as bleaching
    bleaching_time = (total_time - dyeing_time) / 2  # The remaining time is split in half for bleaching

    result = bleaching_time
    return result

print(solution())