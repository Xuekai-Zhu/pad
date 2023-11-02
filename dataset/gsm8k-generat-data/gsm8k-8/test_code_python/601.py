def solution():
    # Convert speeds to feet per second
    cheetah_speed = 60 * 1.5
    gazelle_speed = 40 * 1.5

    # Calculate relative speed
    relative_speed = cheetah_speed - gazelle_speed

    # Calculate time it takes for cheetah to catch up
    distance = 210
    time = distance / relative_speed

    result = time
    return result

print(solution())