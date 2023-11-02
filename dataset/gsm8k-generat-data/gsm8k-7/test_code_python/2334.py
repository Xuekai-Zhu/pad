def solution():
    tank1_goldfish = 7
    tank1_betafish = 8

    tank2_totalfish = 2 * (tank1_goldfish + tank1_betafish)

    tank3_totalfish = tank2_totalfish / 3

    result = tank3_totalfish
    return result

print(solution())