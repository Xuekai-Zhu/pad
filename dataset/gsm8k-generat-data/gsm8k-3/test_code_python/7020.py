def solution():
    """Emberly takes her mornings walks every day. If each walk takes her 1 hour covering 4 miles, and she didn't walk for 4 days in March, calculate the total number of miles she's walked."""
    # Define the time and distance for one walk
    WALK_TIME = 1 # hour
    WALK_DISTANCE = 4 # miles

    # Define the number of walks in March
    MARCH_WALKS = 31 - 4 # 31 days in March, minus 4 days Emberly didn't walk

    # Calculate the total distance walked in March
    total_distance = MARCH_WALKS * WALK_DISTANCE

    # Display the total distance walked
    result = total_distance
    return result

print(solution())