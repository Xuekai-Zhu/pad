def solution():
    tamika_time = 8
    tamika_speed = 45
    logan_time = 5
    logan_speed = 55

    # Calculate the distance traveled by Tamika
    tamika_distance = tamika_time * tamika_speed

    # Calculate the distance traveled by Logan
    logan_distance = logan_time * logan_speed

    # Calculate the difference in distance traveled
    difference = tamika_distance - logan_distance
    result = difference
    return result

print(solution())