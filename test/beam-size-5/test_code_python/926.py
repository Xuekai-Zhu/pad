def solution():
    # Calculate the total number of stuffed animals
    total_stuffed_animals = 31 * 8

    # Calculate the total number of multicolored rings
    total_multicolored_rings = 9

    # Calculate the total number of toys
    total_toys = total_stuffed_animals + total_multicolored_rings

    # Calculate the number of bouncy balls in the tube
    bouncy_balls = 62 - total_toys
    result = bouncy_balls
    return result

print(solution())