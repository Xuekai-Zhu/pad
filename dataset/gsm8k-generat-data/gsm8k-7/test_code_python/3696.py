def solution():
    distance_to_school = 7
    days_per_week = 5

    # Calculate the total distance Christina walks to school every week
    total_distance_to_school = distance_to_school * days_per_week * 2

    # Add the additional 2km for Friday's detour
    total_distance = total_distance_to_school + 2

    result = total_distance
    return result

print(solution())