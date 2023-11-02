def solution():
    # Calculate the distance Benjamin walks to and from work
    work_distance = 2 * 5 * 6  # He walks to work and back 5 days a week, 6 miles each way

    # Calculate the distance Benjamin walks while walking his dog
    dog_distance = 2 * 7 * 2  # He walks his dog twice a day, every day, for 2 miles each time

    # Calculate the distance Benjamin walks to his best friend's house
    friend_distance = 1  # He walks 1 mile to his friend's house once a week

    # Calculate the distance Benjamin walks to the convenience store
    store_distance = 2 * 3  # He walks to the convenience store twice a week, 3 miles each time

    # Calculate the total distance Benjamin walks in a week
    total_distance = work_distance + dog_distance + friend_distance + store_distance
    result = total_distance
    return result

print(solution())