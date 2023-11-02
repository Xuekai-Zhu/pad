def solution():
    """A parking garage of a mall is four stories tall. On the first level, there are 90 parking spaces. The second level has 8 more parking spaces than on the first level, and there are 12 more available parking spaces on the third level than on the second level. The fourth level has 9 fewer parking spaces than the third level. If 100 cars are already parked, how many cars can be accommodated by the parking garage?"""
    # Define the number of parking spaces on each level
    level1_spaces = 90
    level2_spaces = level1_spaces + 8
    level3_spaces = level2_spaces + 12
    level4_spaces = level3_spaces - 9

    # Calculate the total number of parking spaces
    total_spaces = level1_spaces + level2_spaces + level3_spaces + level4_spaces

    # Calculate the number of available parking spaces
    available_spaces = total_spaces - 100

    # Display the number of cars that can be accommodated
    result = available_spaces
    return result

print(solution())