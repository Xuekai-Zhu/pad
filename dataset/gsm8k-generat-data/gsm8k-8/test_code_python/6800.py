def solution():
    # Define the starting number of pencils and the number of pencils lost or broken
    starting_pencils = 20
    lost_pencils = 7
    broken_pencils = 3

    # Subtract the number of lost and broken pencils
    remaining_pencils = starting_pencils - lost_pencils - broken_pencils

    # Add the number of found and purchased pencils
    remaining_pencils += 4 + 2

    result = remaining_pencils
    return result

print(solution())