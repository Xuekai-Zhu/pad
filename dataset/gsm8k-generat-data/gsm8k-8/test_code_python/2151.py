def solution():
    # Define the initial number of pencils
    initial_pencils = 30

    # Calculate how many pencils Charley has after losing 6
    remaining_pencils = initial_pencils - 6

    # Calculate how many pencils Charley has after losing 1/3 of the remaining pencils
    remaining_pencils -= (1/3) * remaining_pencils

    result = remaining_pencils
    return result

print(solution())