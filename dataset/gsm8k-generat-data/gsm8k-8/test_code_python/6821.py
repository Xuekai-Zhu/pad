def solution():
    # Calculate the distance walked to work and back each day (5 days a week)
    work_distance = 2 * 6 * 5

    # Calculate the distance walked with the dog (2 walks a day, 7 days a week)
    dog_distance = 2 * 2 * 7

    # Calculate the distance walked to the friend's house (once a week)
    friend_distance = 1

    # Calculate the distance walked to the convenience store (twice a week)
    store_distance = 2 * 3

    # Calculate the total distance walked in a week
    total_distance = work_distance + dog_distance + friend_distance + store_distance
    result = total_distance
    return result

print(solution())