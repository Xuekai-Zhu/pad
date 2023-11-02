def solution():
    """Mark and James need a total of 14 dice that are 12 sided to play their game.
    Mark has a bag of 10 dice and 60% of them are 12 sided.
    James has a bag of 8 dice and 75% of them are 12 sided.
    How many dice will the boys need to buy to play their game?"""
    # Define the total number of dice needed
    total_dice_needed = 14

    # Calculate the number of 12-sided dice that Mark has
    mark_dice = 10
    mark_12sided_dice = mark_dice * 0.6

    # Calculate the number of 12-sided dice that James has
    james_dice = 8
    james_12sided_dice = james_dice * 0.75

    # Calculate the total number of 12-sided dice that they have
    total_12sided_dice = mark_12sided_dice + james_12sided_dice

    # Calculate the number of additional dice they need to buy
    additional_dice_needed = total_dice_needed - total_12sided_dice

    # return the result
    result = additional_dice_needed
    return result

print(solution())