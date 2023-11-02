def solution():
    # Calculate the time for each step in years
    acclimation = 1
    basics = 2
    research = 2.75 * basics
    dissertation = 0.5 * acclimation

    # Calculate the total time in years
    total_time = acclimation + basics + research + dissertation
    result = total_time
    return result

print(solution())