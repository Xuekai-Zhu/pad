def solution():
    # Define Oliver's reading speed
    oliver_speed = 40

    # Define Lucy's reading speed using Oliver's speed
    lucy_speed = oliver_speed + 20

    # Define Carter's reading speed as half of Lucy's speed
    carter_speed = lucy_speed / 2

    result = carter_speed
    return result

print(solution())