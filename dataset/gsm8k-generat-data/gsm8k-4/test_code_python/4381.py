def solution():
    """Danny has three picnic blankets. When they are unfolded they each have an area of 8 x 8. After he folds them, their total area is 48 square feet. How many times did he fold them?"""
    # Define the area of each unfolded blanket
    unfolded_area = 8 * 8

    # Define the total area of the folded blankets
    folded_area = 48

    # Calculate the total number of blankets
    total_blankets = folded_area / unfolded_area

    # Calculate the number of folds per blanket
    folds_per_blanket = 4

    # Calculate the total number of folds
    total_folds = total_blankets * folds_per_blanket

    result = total_folds
    return result

print(solution())