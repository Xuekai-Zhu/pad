def solution():
    # Calculate the time it took for George's turtle to finish the race
    greta_time = 6  # minutes
    george_time = greta_time - 2  # George's turtle finished 2 minutes quicker than Greta's

    # Calculate the time it took for Gloria's turtle to finish the race
    gloria_time = 2 * george_time  # Gloria's turtle took twice as long as George's turtle

    result = gloria_time
    return result

print(solution())