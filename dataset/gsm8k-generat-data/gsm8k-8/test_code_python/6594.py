def solution():
    # Define the total number of paper plates needed
    total_plates_needed = 65

    # Define the number of plates Max already has
    green_plates = 22
    blue_plates = 24
    total_plates_owned = green_plates + blue_plates

    # Calculate the number of plates Max still needs to buy
    plates_needed = total_plates_needed - total_plates_owned
    result = plates_needed
    return result

print(solution())