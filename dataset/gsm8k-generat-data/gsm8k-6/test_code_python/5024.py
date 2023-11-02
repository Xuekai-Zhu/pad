def solution():
    initial_time = 8  # initial number of hours John can run
    increased_time = initial_time * 1.75  # number of hours John can run after increasing by 75%
    initial_speed = 8  # initial speed in mph
    increased_speed = initial_speed + 4  # speed after increasing by 4 mph
    distance_initial = initial_speed * initial_time  # distance covered initially
    distance_increased = increased_speed * increased_time  # distance covered after increasing time and speed
    result = distance_increased
    return result

print(solution())