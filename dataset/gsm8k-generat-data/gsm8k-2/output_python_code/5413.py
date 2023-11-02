def solution():
    """Peter has to walk 2.5 miles to get to the grocery store. If it takes him 20 minutes to walk one mile and he has walked 1 mile already, how many more minutes does he have to walk to reach it?"""
    total_distance = 2.5
    time_per_mile = 20
    distance_left = total_distance - 1
    time_left = distance_left * time_per_mile
    result = time_left
    return result

print(solution())