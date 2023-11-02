def solution():
    """Danny has three picnics blankets. When they are unfolded they each have an area of 8 x 8. After he folds them up, their total area is 48 square feet. How many times did he fold them?"""
    # Define the area of one unfolded blanket
    blanket_area_unfolded = 8 * 8

    # Calculate the total area of all three blankets unfolded
    total_area_unfolded = blanket_area_unfolded * 3

    # Calculate the total number of times the blankets were folded
    folds = 0
    total_area_folded = total_area_unfolded
    while total_area_folded > 48:
        folds += 1
        total_area_folded /= 2

    # Display the number of folds
    result = folds
    return result

print(solution())