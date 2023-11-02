def solution():
    # Determine the speed of the spaceship with 200 people on board
    speed_200 = 500

    # Determine the number of times the speed is halved with 200 more people on board
    halving_factor = 2 ** (200 // 100)

    # Determine the speed of the spaceship with 400 people on board
    speed_400 = speed_200 / halving_factor * (2 ** (400 // 100))

    result = speed_400
    return result

print(solution())