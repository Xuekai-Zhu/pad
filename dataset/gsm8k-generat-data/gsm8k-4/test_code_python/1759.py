def solution():
    """Jason drives past 3 convenience stores on his way to work. The distance between the first store and the second store is 6 miles. The distance between the second store and third store is 2/3rds longer than the distance between the first two stores. The distance from his house to the first store and the last store to work is the same, 4 miles. How long in miles is Jason's commute to work?"""
    # Define the distances
    dist_1_2 = 6
    dist_2_3 = dist_1_2 + (2/3)*dist_1_2
    dist_home_to_store = 4

    # Calculate the total distance of the commute
    total_dist = dist_home_to_store + dist_1_2 + dist_2_3 + dist_home_to_store

    # Return the result
    result = total_dist
    return result

print(solution())