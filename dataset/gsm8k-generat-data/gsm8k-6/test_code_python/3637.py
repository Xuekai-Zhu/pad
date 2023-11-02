def solution():
    # Calculate the fewest number of trips Gretchen must take to carry all 17 objects to the boat
    trips_to_surface = 17 // 3  # divide 17 by 3 and round down to get the number of full trips
    if 17 % 3 != 0:  # if there are remaining objects after full trips
        trips_to_surface += 1  # add one more trip to carry the remaining objects
    result = trips_to_surface
    return result

print(solution())