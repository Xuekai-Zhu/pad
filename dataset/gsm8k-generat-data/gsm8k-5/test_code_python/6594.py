def solution():
    # Total number of paper plates Max needs
    total_paper_plates = 65

    # Number of paper plates Max already has
    green_plates = 22
    blue_plates = 24
    plates_already_have = green_plates + blue_plates

    # Calculate the number of paper plates Max still needs
    plates_needed = total_paper_plates - plates_already_have
    result = plates_needed
    return result

print(solution())