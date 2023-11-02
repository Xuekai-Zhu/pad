def solution():
    # Calculate the total distance of Jason's commute to work
    distance_to_second_store = 6  # distance between the first and second store
    distance_to_third_store = distance_to_second_store + (2/3)*distance_to_second_store  # distance between the second and third store
    distance_from_house_to_first_store = 4
    distance_from_last_store_to_work = 4

    total_distance = distance_to_second_store + distance_to_third_store + distance_from_house_to_first_store + distance_from_last_store_to_work
    result = total_distance
    return result

print(solution())