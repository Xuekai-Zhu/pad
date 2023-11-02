def solution():
    home_to_store_time = 2
    store_to_friend_time = 1
    distance_to_friend = 50

    # Calculate the time it takes to go from the store to the friend
    time_to_friend = store_to_friend_time / 2

    # Calculate the distance from the home to the store
    distance_home_to_store = distance_to_friend / (2 * home_to_store_time)

    # Calculate the total distance traveled by Peter and Jack
    total_distance = 2 * (distance_home_to_store + distance_to_friend)

    result = total_distance
    return result

print(solution())