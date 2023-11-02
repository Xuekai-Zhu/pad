def solution():
    total_needed = 65
    green_plates = 22
    blue_plates = 24

    # Calculate the total number of paper plates Max already has
    total_owned = green_plates + blue_plates

    # Calculate the number of paper plates Max still needs
    plates_needed = total_needed - total_owned
    result = plates_needed
    return result

print(solution())