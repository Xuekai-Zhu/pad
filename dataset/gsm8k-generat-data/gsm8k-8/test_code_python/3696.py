def solution():
    # Calculate the distance Christina walks to school and back each day
    daily_distance = 2 * 7

    # Calculate the total distance Christina walks to school and back for the five days
    total_distance = 5 * daily_distance

    # Add the extra 2km from Friday's detour
    total_distance += 2

    result = total_distance
    return result

print(solution())