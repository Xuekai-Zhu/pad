def solution():
    """Danny has three picnics blankets. When they are unfolded they each have an area of 8 x 8. After he folds them up, their total area is 48 square feet. How many times did he fold them?"""
    unfold_area = 8 * 8
    total_unfold_area = unfold_area * 3
    total_fold_area = 48
    fold_ratio = total_unfold_area / total_fold_area
    num_folds = round(math.log(fold_ratio, 2))
    result = num_folds
    return result

print(solution())