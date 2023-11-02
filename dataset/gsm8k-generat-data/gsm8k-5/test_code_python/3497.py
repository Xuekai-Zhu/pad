def solution():
    time_for_emma = 20  # Emma can run both arenas in 20 hours
    time_for_fernando = 2 * time_for_emma  # Fernando takes twice as long to run his course

    # Calculate the total time it takes both of them to run all around the two arenas
    total_time = time_for_emma + time_for_fernando
    result = total_time
    return result

print(solution())