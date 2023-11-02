def solution():
    speed_alone = 4  # John runs at 4 miles per hour when alone
    speed_with_dog = 6  # John runs at 6 miles per hour when with his dog
    dog_weight = 100  # John's dog weighs 100 pounds

    # Calculate the distance John and his dog run together in 30 minutes
    distance_with_dog = (speed_with_dog * 0.5) + (0.5 * (speed_with_dog - speed_alone) * (dog_weight/150))

    # Calculate the distance John runs alone in 30 minutes
    distance_alone = speed_alone * 0.5

    # Calculate the total distance John travels
    total_distance = distance_with_dog + distance_alone
    result = total_distance
    return result

print(solution())