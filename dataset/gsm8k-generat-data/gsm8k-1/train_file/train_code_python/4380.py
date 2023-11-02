def solution():
    """Danny has three picnics blankets. When they are unfolded they each have an area of 8 x 8. After he folds them, their total area is 48 square feet. How many times did he fold them?"""
    blanket_area = 8*8
    total_area = 48
    folded_area = blanket_area/2
    folded_blankets = total_area/folded_area
    folds_per_blanket = 2
    total_folds = folded_blankets * folds_per_blanket
    result = total_folds
    return result

print(solution())