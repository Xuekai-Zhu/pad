def solution():
    math_time = 15 * 2  # Brooke spends 2 minutes on each math problem
    ss_time = 6 * 0.5  # Brooke spends 30 seconds on each social studies problem
    science_time = 10 * 1.5  # Brooke spends 1.5 minutes on each science problem

    # Calculate the total time it will take Brooke to answer all his homework
    total_time = (math_time + ss_time + science_time) / 60  # Convert total time to minutes
    result = total_time
    return result

print(solution())