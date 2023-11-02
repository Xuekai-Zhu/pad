def solution():
    """Mark and James need a total of 14 dice that are 12 sided to play their game.  Mark has a bag of 10 dice and 60% of them are 12 sided.  James has a bag of 8 dice and 75% of them are 12 sided.  How many dice will the boys need to buy to play their game?"""
    # Mark's dice
    mark_total_dice = 10
    mark_twelve_sided_dice = int(mark_total_dice * 0.6)

    # James's dice
    james_total_dice = 8
    james_twelve_sided_dice = int(james_total_dice * 0.75)

    # Total twelve sided dice needed
    total_twelve_sided_dice_needed = 14

    # Calculate number of dice to be bought
    dice_to_be_bought = total_twelve_sided_dice_needed - mark_twelve_sided_dice - james_twelve_sided_dice

    # Display the number of dice to be bought
    result = dice_to_be_bought
    return result

print(solution())