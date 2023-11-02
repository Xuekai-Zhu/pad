def solution():
    xena_start = 600  # Xena has a 600 foot head start
    danger_zone = 120  # The dragon can burn Xena if it gets within 120 feet of her
    xena_speed = 15  # Xena runs 15 feet per second
    dragon_speed = 30  # The dragon flies 30 feet per second

    # Calculate the distance Xena needs to run to reach the safety of the cave
    required_distance = xena_start + danger_zone

    # Calculate the time Xena has to get to the cave
    time = required_distance / (xena_speed + dragon_speed)
    result = time
    return result

print(solution())