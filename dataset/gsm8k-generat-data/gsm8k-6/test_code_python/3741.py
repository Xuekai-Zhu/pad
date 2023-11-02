def solution():
    # Calculate the number of steps Roger needs to walk
    steps_to_walk = 10000 - 2000  # Roger has already walked 2000 steps during his lunch break

    # Calculate the amount of time needed to walk the remaining steps
    time_needed = (steps_to_walk / 2000) * 30  # Roger can walk 2000 steps in 30 minutes
    result = time_needed
    return result

print(solution())