def solution():
    """Benjamin is tracking how many miles he walks in a week. He walks to work and home five days a week, walks his dog twice a day every day, walks to his best friend’s house once a week, and walks to the convenience store twice a week. Work is six miles away, dog walks are two miles, his best friend’s house is one mile, and the convenience store is three miles. How many miles does Benjamin walk in a week?"""
    work_distance = 6 * 2 * 5
    dog_distance = 2 * 2 * 7
    friend_distance = 1
    store_distance = 3 * 2
    total_distance = work_distance + dog_distance + friend_distance + store_distance
    result = total_distance
    return result

print(solution())