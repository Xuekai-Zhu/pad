def solution():
    """Jason drives past 3 convenience stores on his way to work. The distance between the first store and the second store is 6 miles. The distance between the second store and third store is 2/3rds longer than the distance between the first two stores. The distance from his house to the first store and the last store to work is the same, 4 miles. How long in miles is Jason's commute to work?"""
    # Define the distances between the stores
    distance_1_2 = 6
    distance_2_3 = distance_1_2 + (2/3)*distance_1_2

    # Define the distance from Jason's house to the first store and from the last store to work
    distance_home_store = 4

    # Calculate the total distance of Jason's commute
    total_distance = distance_home_store + distance_1_2 + distance_2_3 + distance_home_store

    # Display the total distance
    result = total_distance
    return result

print(solution())