def solution():
    """ Benjamin is tracking how many miles he walks in a week. He walks to work and home five days a week, walks his dog twice a day every day, walks to his best friend’s house once a week, and walks to the convenience store twice a week. Work is six miles away, dog walks are two miles, his best friend’s house is one mile, and the convenience store is three miles. How many miles does Benjamin walk in a week? """
    # Define the distances
    WORK_DIST = 6
    DOG_DIST = 2
    FRIEND_DIST = 1
    STORE_DIST = 3

    # Define the number of trips
    WORK_TRIPS = 5
    DOG_TRIPS = 2 * 7
    FRIEND_TRIPS = 1
    STORE_TRIPS = 2

    # Calculate the total distance
    total_dist = WORK_DIST * 2 * WORK_TRIPS + DOG_DIST * DOG_TRIPS + FRIEND_DIST * FRIEND_TRIPS + STORE_DIST * STORE_TRIPS

    # Display the total distance
    result = total_dist
    return result

print(solution())