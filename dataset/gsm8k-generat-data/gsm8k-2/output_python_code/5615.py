def solution():
    """Xena is trying to outrun a dragon to get to the safety of a cave it's too big to fit into. Xena has a 600 foot head start, but the dragon can burn her if it gets within 120 feet of her. If Xena runs 15 feet per second and the dragon flies 30 feet per second, how many seconds does Xena have to get to the cave?"""
    xena_distance = 600
    dragon_distance = 0
    safety_distance = 120
    xena_speed = 15
    dragon_speed = 30
    time = 0
    while xena_distance > (dragon_distance + safety_distance):
        xena_distance -= xena_speed
        dragon_distance += dragon_speed
        time += 1
    result = time
    return result

print(solution())