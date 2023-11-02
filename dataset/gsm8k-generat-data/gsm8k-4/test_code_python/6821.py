def solution():
    """Benjamin is tracking how many miles he walks in a week. He walks to work and home five days a week, walks his dog twice a day every day, walks to his best friend’s house once a week, and walks to the convenience store twice a week. Work is six miles away, dog walks are two miles, his best friend’s house is one mile, and the convenience store is three miles. How many miles does Benjamin walk in a week?"""
    # Define the distances walked to work and home
    work_distance = 6
    total_work_distance = work_distance * 2 * 5

    # Define the distances walked for dog walks
    dog_walk_distance = 2
    total_dog_walk_distance = dog_walk_distance * 2 * 7

    # Define the distance walked to his best friend's house
    best_friend_distance = 1

    # Define the distance walked to the convenience store
    convenience_store_distance = 3
    total_convenience_store_distance = convenience_store_distance * 2

    # Calculate the total distance walked in a week
    total_distance = total_work_distance + total_dog_walk_distance + best_friend_distance + total_convenience_store_distance

    result = total_distance
    return result

print(solution())