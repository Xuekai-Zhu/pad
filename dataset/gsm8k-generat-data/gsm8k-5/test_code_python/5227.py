def solution():
    # Calculate the number of legos needed for two identical airplanes
    legos_per_airplane = 240
    legos_needed = 2 * legos_per_airplane

    # Calculate the number of legos Julian still needs
    legos_remaining = legos_needed - 400
    result = legos_remaining
    return result

print(solution())