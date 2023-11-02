def solution():
    """The pirates plan to explore 4 islands. Two islands require walking 20 miles per day while the other two islands require 25 miles per day. How many miles will they have to walk if it takes 1.5 days to explore each island?"""
    # Define the number of islands and the walking distances per day
    NUM_ISLANDS = 4
    LONG_DISTANCE = 25
    SHORT_DISTANCE = 20

    # Define the number of days it takes to explore each island
    DAYS_PER_ISLAND = 1.5

    # Calculate the total distance walked on the two long distance islands
    long_distance_total = LONG_DISTANCE * 2 * DAYS_PER_ISLAND

    # Calculate the total distance walked on the two short distance islands
    short_distance_total = SHORT_DISTANCE * 2 * DAYS_PER_ISLAND

    # Calculate the total distance walked on all four islands
    total_distance = long_distance_total + short_distance_total

    # Display the total distance walked
    result = total_distance
    return result

print(solution())