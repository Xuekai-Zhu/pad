def solution():
    """Emmy has a collection of 14 iPods. She loses 6 out of the 14 she had but she still has twice as many as Rosa. How many iPods does Emmy and Rosa have together?"""
    # Define the initial number of iPods Emmy had
    initial_iPods = 14

    # Define the number of iPods Emmy lost
    lost_iPods = 6

    # Define the number of iPods Emmy has left
    remaining_iPods = initial_iPods - lost_iPods

    # Define the number of iPods Rosa has
    rosa_iPods = remaining_iPods / 2

    # Calculate the total number of iPods
    total_iPods = remaining_iPods + rosa_iPods

    result = total_iPods
    return result

print(solution())