def solution():
    # Calculate the total number of dice Mark and James have
    dice_mark = 10  # Mark has a bag of 10 dice
    dice_james = 8  # James has a bag of 8 dice
    dice_total = dice_mark + dice_james

    # Calculate how many 12-sided dice Mark has and how many James has
    dice_mark_12sided = int(dice_mark * 0.6)  # 60% of Mark's dice are 12-sided
    dice_james_12sided = int(dice_james * 0.75)  # 75% of James's dice are 12-sided

    # Calculate the total number of 12-sided dice Mark and James have
    dice_12sided_total = dice_mark_12sided + dice_james_12sided

    # Calculate how many more 12-sided dice Mark and James need to play their game
    dice_needed = 14 - dice_12sided_total

    result = dice_needed
    return result

print(solution())