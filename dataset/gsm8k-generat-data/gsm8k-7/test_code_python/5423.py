def solution():
    distance_skated = 10
    distance_walked = 4

    # John has to skate the same distance back home, so total distance skated = 2 * distance_skated
    total_distance_skated = 2 * distance_skated

    # Add the distance walked to the total distance skated to find the total distance John traveled
    total_distance = total_distance_skated + distance_walked
    result = total_distance_skated
    return result

print(solution())