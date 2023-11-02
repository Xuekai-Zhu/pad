def solution():
    num_chickens = 7
    num_sheep = 5

    # Calculate the total number of legs from the chickens
    chicken_legs = num_chickens * 2

    # Calculate the total number of legs from the sheep
    sheep_legs = num_sheep * 4

    # Calculate the total number of legs among all the animals
    total_legs = chicken_legs + sheep_legs
    result = total_legs
    return result

print(solution())