def solution():
    # Calculate the total time it takes for Gunther to clean his apartment
    total_time = (45 + 60 + 30 + (5*3))  # in minutes

    # Calculate the amount of free time Gunther will have after cleaning his apartment
    free_time = (3 * 60) - total_time  # 3 hours of free time expressed in minutes, minus the total time it takes to clean the apartment
    
    result = free_time
    return result

print(solution())