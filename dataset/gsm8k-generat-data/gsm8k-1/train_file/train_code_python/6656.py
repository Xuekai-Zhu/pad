def solution():
    """Mark and James need a total of 14 dice that are 12 sided to play their game. Mark has a bag of 10 dice and 60% of them are 12 sided. James has a bag of 8 dice and 75% of them are 12 sided. How many dice will the boys need to buy to play their game?"""
    mark_dice = 10
    mark_12_sided = 0.6 * mark_dice
    james_dice = 8
    james_12_sided = 0.75 * james_dice
    total_12_sided = mark_12_sided + james_12_sided
    dice_needed = 14 - total_12_sided
    result = dice_needed
    return result

print(solution())