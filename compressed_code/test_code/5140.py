def solution():
    
    mark_dice = 10
    mark_twelve_sided = 0.6 * mark_dice
    james_dice = 8
    james_twelve_sided = 0.75 * james_dice
    total_twelve_sided = mark_twelve_sided + james_twelve_sided
    dice_needed = 14 - total_twelve_sided
    result = dice_needed
    return result

print(solution())