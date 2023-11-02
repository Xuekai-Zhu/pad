def solution():
    num_ignatius_bikes = 4
    num_friend_tires = 3 * num_ignatius_bikes + 1  # friend has one unicycle and one tricycle
    num_friend_bikes = (num_friend_tires - 1) // 2  # each bike has 2 tires, subtracting the unicycle
    result = num_friend_bikes
    return result

print(solution())