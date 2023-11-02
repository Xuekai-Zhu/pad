def solution():
    # Define Renaldo's distance
    renaldo_distance = 15

    # Calculate Ernesto's distance
    ernesto_distance = (1/3) * renaldo_distance + 7

    # Calculate the total distance
    total_distance = renaldo_distance + ernesto_distance

    result = total_distance
    return result

print(solution())