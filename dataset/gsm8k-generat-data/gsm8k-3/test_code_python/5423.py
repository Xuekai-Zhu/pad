def solution():
    """John skateboarded for 10 miles and then walked another 4 miles to the park. He then skated all the way back home. How many miles has John skateboarded in total?"""
    # Define the distance John walked to the park
    WALKING_DISTANCE = 4

    # Calculate the total distance John skateboarded
    SKATEBOARD_DISTANCE = 2 * (10 + WALKING_DISTANCE)

    # Display the total distance
    result = SKATEBOARD_DISTANCE
    return result

print(solution())