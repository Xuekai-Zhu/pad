def solution():
    # Calculate the number of pencils Charley currently has
    remaining_pencils = 30 - 6  # Charley lost 6 pencils while moving to school
    lost_pencils = (1/3) * remaining_pencils  # Charley lost 1/3 of the remaining pencils
    current_pencils = remaining_pencils - lost_pencils  # Calculate the current number of pencils
    result = current_pencils
    return result

print(solution())