def solution():
    # Calculate the number of tents in each part of the campsite
    north = 100
    east = 2 * north
    center = 4 * north
    south = 200

    # Calculate the total number of tents in the recreation area
    total_tents = north + east + center + south
    result = total_tents
    return result

print(solution())