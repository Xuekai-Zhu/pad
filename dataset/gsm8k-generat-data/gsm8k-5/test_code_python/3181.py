def solution():
    sheep_speed = 12  # Sheep can run 12 feet per second
    dog_speed = 20  # Sheepdog can run 20 feet per second
    distance = 160  # The sheep is 160 feet away from the sheepdog

    # Calculate how long it takes the dog to catch the sheep
    time = distance / (dog_speed - sheep_speed)
    result = time
    return result

print(solution())