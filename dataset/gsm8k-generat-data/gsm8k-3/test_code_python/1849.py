def solution():
    """Jennifer wants to go to a museum. There is one 5 miles away from her home and one 15 miles away. If Jennifer goes to both museums on two separate days, how many miles total will she travel?"""
    # Define the distances to each museum
    MUSEUM_1_DISTANCE = 5
    MUSEUM_2_DISTANCE = 15

    # Calculate the total distance traveled
    total_distance = 2 * (MUSEUM_1_DISTANCE + MUSEUM_2_DISTANCE)

    # Display the total distance traveled
    result = total_distance
    return result

print(solution())