def solution():
    thor_age = 1456

    # Calculate Captain America's age
    cap_america_age = thor_age / 13

    # Calculate Peter Parker's age
    peter_parker_age = cap_america_age / 7

    # Calculate Ironman's age
    ironman_age = peter_parker_age + 32
    result = ironman_age
    return result

print(solution())