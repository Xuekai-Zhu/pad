def solution():
    # Calculate the number of streetlights that will be used in the squares
    used_streetlights = 15 * 12  # each park will have 12 new streetlights

    # Calculate the number of unused streetlights
    unused_streetlights = 200 - used_streetlights
    result = unused_streetlights
    return result

print(solution())