def solution():
    # Calculate the number of calories Kiley ate
    calories_ate = 0.25 * 2800  # Kiley ate 25% of the cheesecake
    # Calculate the number of slices Kiley ate
    slices_ate = calories_ate / 350  # each slice contains 350 calories
    result = slices_ate
    return result

print(solution())