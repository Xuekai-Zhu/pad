def solution():
    distance_first_second_store = 6
    distance_second_third_store = distance_first_second_store * (2/3 + 1)  # 2/3 longer than previous distance
    distance_house_first_store = distance_last_store_work = 4

    # Calculate the total distance of Jason's commute
    total_distance = distance_first_second_store + distance_second_third_store + distance_house_first_store + distance_last_store_work
    result = total_distance
    return result

print(solution())