def solution():
    """John jogs at a speed of 4 miles per hour when he runs alone, but runs at 6 miles per hour when he is being dragged by his 100-pound German Shepherd dog. If John and his dog go on a run together for 30 minutes, and then John runs for an additional 30 minutes by himself, how far will John have traveled?"""
    # Convert speeds to miles per minute
    john_speed_alone = 4 / 60
    john_speed_with_dog = 6 / 60

    # Calculate distances
    john_distance_with_dog = john_speed_with_dog * (30 / 60)
    john_distance_alone = john_speed_alone * (30 / 60)

    # Total distance
    total_distance = john_distance_with_dog + john_distance_alone

    result = total_distance
    return result

print(solution())