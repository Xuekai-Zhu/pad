def solution():
    """Susan has 3 fish tanks to fill. 1 fish tank contains 7 goldfish and 8 beta fish. The second fish tank contains twice as many fish as the first tank and the third fish tank has a third of the number of fish in the second fish tank. How many fish are in the third fish tank?"""
    # Define the number of fish in the first tank
    first_tank = 7 + 8

    # Define the number of fish in the second tank
    second_tank = first_tank * 2

    # Define the number of fish in the third tank
    third_tank = second_tank // 3

    # Display the number of fish in the third tank
    result = third_tank
    return result

print(solution())