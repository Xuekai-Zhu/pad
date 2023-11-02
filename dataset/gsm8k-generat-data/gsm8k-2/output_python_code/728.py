def solution():
    """John jogs at a speed of 4 miles per hour when he runs alone, but runs at 6 miles per hour when he is being dragged by his 100-pound German Shepherd dog. If John and his dog go on a run together for 30 minutes, and then John runs for an additional 30 minutes by himself, how far will John have traveled?"""
    john_speed_alone = 4
    john_speed_dog = 6
    dog_weight = 100
    total_time = 60  # 30 + 30 minutes
    john_distance_with_dog = (john_speed_dog * total_time / 60) * (dog_weight / (john_speed_alone + john_speed_dog))
    john_distance_alone = (john_speed_alone * total_time / 60) - john_distance_with_dog
    total_distance = john_distance_with_dog + john_distance_alone
    result = total_distance
    return result

print(solution())