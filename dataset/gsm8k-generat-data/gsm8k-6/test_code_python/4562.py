def solution():
    # Calculate the number of holes that are filled with dirt
    filled_holes = round(8 * 0.75)  # 75% of 8 holes are filled

    # Calculate the number of unfilled holes
    unfilled_holes = 8 - filled_holes

    result = unfilled_holes
    return result

print(solution())