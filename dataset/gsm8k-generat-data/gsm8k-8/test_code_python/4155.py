def solution():
    # Define the initial number of iPods Emmy had
    emmy_initial = 14

    # Calculate the number of iPods Emmy has after losing 6
    emmy_final = emmy_initial - 6

    # Calculate the number of iPods Rosa has
    rosa = emmy_final / 2

    # Calculate the total number of iPods they have together
    total = emmy_final + rosa
    result = total
    return result

print(solution())