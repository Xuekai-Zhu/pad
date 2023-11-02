def solution():
    """Max needs 65 paper plates for the barbecue party.  He already has 22 green paper plates and 24 blue paper plates. How many more paper plates does he need?"""
    # Define the total number of paper plates Max needs
    total_plates_needed = 65

    # Define the number of green and blue paper plates Max already has
    green_plates = 22
    blue_plates = 24

    # Calculate the total number of paper plates Max already has
    plates_already_have = green_plates + blue_plates

    # Calculate the number of paper plates Max still needs
    plates_needed = total_plates_needed - plates_already_have

    # Display the number of paper plates Max still needs
    result = plates_needed
    return result

print(solution())