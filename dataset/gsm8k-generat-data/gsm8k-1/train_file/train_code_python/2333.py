def solution():
    """Susan has 3 fish tanks to fill. 1 fish tank contains 7 goldfish and 8 beta fish. The second fish tank contains twice as many fish as the first tank and the third fish tank has a third of the number of fish in the second fish tank. How many fish are in the third fish tank?"""
    tank1_fish = 7 + 8
    tank2_fish = tank1_fish * 2
    tank3_fish = tank2_fish // 3
    result = tank3_fish
    return result

print(solution())