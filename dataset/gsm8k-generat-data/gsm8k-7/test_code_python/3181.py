def solution():
    sheep_speed = 12
    dog_speed = 20
    distance = 160

    # Calculate the time it takes for the dog to catch the sheep
    relative_speed = dog_speed - sheep_speed
    time = distance / relative_speed
    result = time
    return result

print(solution())