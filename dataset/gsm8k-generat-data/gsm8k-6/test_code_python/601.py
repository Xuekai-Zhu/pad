def solution():
    # Convert speeds from miles per hour to feet per second
    cheetah_speed = 60 * 1.5  # 1 mile per hour is about 1.5 feet per second
    gazelle_speed = 40 * 1.5
    # Calculate the relative speed between the cheetah and gazelle
    relative_speed = cheetah_speed - gazelle_speed
    # Calculate the time it takes for the cheetah to catch up to the gazelle
    time = 210 / relative_speed
    result = time
    return result

print(solution())