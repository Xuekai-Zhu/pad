def solution():
    """John jogs at a speed of 4 miles per hour when he runs alone, but runs at 6 miles per hour when he is being dragged by his 100-pound German Shepherd dog. If John and his dog go on a run together for 30 minutes, and then John runs for an additional 30 minutes by himself, how far will John have traveled?"""
    # Define John's speeds
    SOLO_SPEED = 4 # mph
    DOG_SPEED = 6 # mph

    # Define the time John spends running with his dog and running solo
    GROUP_TIME = 0.5 # hours
    SOLO_TIME = 0.5 # hours

    # Calculate the distance John runs with his dog
    group_distance = DOG_SPEED * GROUP_TIME

    # Calculate the distance John runs solo
    solo_distance = SOLO_SPEED * SOLO_TIME

    # Calculate the total distance John travels
    total_distance = group_distance + solo_distance

    # Display the total distance
    result = total_distance
    return result

print(solution())