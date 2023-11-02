def solution():
    total_needed = 84
    green_plates = 21
    red_plates = 28

    # Calculate how many plates Xavier already has
    total_existing = green_plates + red_plates

    # Calculate how many more plates Xavier needs
    plates_needed = total_needed - total_existing
    result = plates_needed
    return result

print(solution())