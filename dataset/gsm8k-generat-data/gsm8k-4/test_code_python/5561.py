def solution():
    """The pirates plan to explore 4 islands. Two islands require walking 20 miles per day while the other two islands require 25 miles per day. How many miles will they have to walk if it takes 1.5 days to explore each island?"""
    # Define the distances for each type of island
    short_distance = 20
    long_distance = 25

    # Define the number of islands for each type
    short_islands = 2
    long_islands = 2

    # Define the number of days it takes to explore each island
    days_per_island = 1.5

    # Calculate the total distance for the short islands
    short_distance_total = short_distance * short_islands * days_per_island

    # Calculate the total distance for the long islands
    long_distance_total = long_distance * long_islands * days_per_island

    # Calculate the total distance they will have to walk
    total_distance = short_distance_total + long_distance_total

    result = total_distance
    return result

print(solution())