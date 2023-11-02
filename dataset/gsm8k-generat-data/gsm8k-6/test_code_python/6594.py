def solution():
    # Calculate the number of paper plates Max still needs
    total_plates = 65  # total number of paper plates Max needs
    green_plates = 22  # number of green paper plates Max already has
    blue_plates = 24  # number of blue paper plates Max already has

    plates_left = total_plates - green_plates - blue_plates
    result = plates_left
    return result

print(solution())