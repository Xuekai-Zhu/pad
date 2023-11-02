def solution():
    dice_per_person = 4  # Tom and Tim each have 4 dice
    sides_per_dice = 6  # Each die has 6 sides

    # Calculate the total number of sides
    total_sides = dice_per_person * 2 * sides_per_dice
    result = total_sides
    return result

print(solution())