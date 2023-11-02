def solution():
    """Susan has 3 fish tanks to fill. 1 fish tank contains 7 goldfish and 8 beta fish. The second fish tank contains twice as many fish as the first tank and the third fish tank has a third of the number of fish in the second fish tank. How many fish are in the third fish tank?"""
    first_tank = 7 + 8
    second_tank = 2 * first_tank
    third_tank = second_tank / 3
    result = third_tank
    return result

print(solution())