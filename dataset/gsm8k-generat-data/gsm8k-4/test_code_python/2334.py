def solution():
    """Susan has 3 fish tanks to fill. 1 fish tank contains 7 goldfish and 8 beta fish. The second fish tank contains twice as many fish as the first tank and the third fish tank has a third of the number of fish in the second fish tank. How many fish are in the third fish tank?"""
    # Calculate the total number of fish in the first tank
    first_tank_fish = 7 + 8

    # Calculate the total number of fish in the second tank
    second_tank_fish = first_tank_fish * 2

    # Calculate the total number of fish in the third tank
    third_tank_fish = second_tank_fish / 3

    # Return the result
    result = third_tank_fish
    return result

print(solution())