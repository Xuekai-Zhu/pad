def solution():
    distance_to_school = 7  # Christina walks 7km to school
    total_distance = distance_to_school * 2 * 5  # Christina walks to school and back for 5 days a week
    extra_distance = 2  # Christina walks an extra 2km to her mother's friend's house

    # Calculate the total distance Christina covered for the week
    total_distance += extra_distance
    result = total_distance
    return result

print(solution())