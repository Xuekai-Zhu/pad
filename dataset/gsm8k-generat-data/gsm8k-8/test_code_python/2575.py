def solution():
    # Define the total distance and number of equal portions
    total_distance = 35
    num_portions = 5

    # Calculate the distance of each portion
    portion_distance = total_distance / num_portions

    # Calculate the distance Abel has traveled after 0.7 hours
    distance_traveled = 40 * 0.7

    # Calculate the number of portions Abel has covered
    portions_covered = distance_traveled / portion_distance
    result = portions_covered
    return result

print(solution())