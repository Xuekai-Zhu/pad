def solution():
    """Max needs 65 paper plates for the barbecue party. He already has 22 green paper plates and 24 blue paper plates. How many more paper plates does he need?"""
    # Define the total number of paper plates needed
    total_plates_needed = 65

    # Calculate the number of plates Max already has
    plates_max_has = 22 + 24

    # Calculate the number of plates Max still needs
    plates_needed = total_plates_needed - plates_max_has

    # return the result
    result = plates_needed
    return result

print(solution())