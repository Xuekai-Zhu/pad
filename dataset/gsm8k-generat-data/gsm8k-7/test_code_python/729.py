def solution():
    john_speed_alone = 4  # mph
    john_speed_with_dog = 6  # mph
    dog_weight = 100  # lbs
    total_time = 1 # hour (30 minutes with dog + 30 minutes alone)

    # Calculate the distance traveled during the 30 minutes with the dog
    distance_with_dog = (john_speed_with_dog * dog_weight * total_time) / (dog_weight + 160)

    # Calculate the distance traveled during the 30 minutes alone
    distance_alone = john_speed_alone * (total_time - 0.5)

    # Calculate the total distance traveled
    total_distance = distance_with_dog + distance_alone
    result = total_distance
    return result

print(solution())