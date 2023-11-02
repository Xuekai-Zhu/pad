def solution():
    # Calculate the number of 12-sided dice in Mark's bag
    mark_dice = 10
    mark_12sided_dice = 0.6 * mark_dice

    # Calculate the number of 12-sided dice in James's bag
    james_dice = 8
    james_12sided_dice = 0.75 * james_dice

    # Calculate the total number of 12-sided dice the boys have
    total_12sided_dice = mark_12sided_dice + james_12sided_dice

    # Calculate how many more dice the boys need to buy
    additional_dice = 14 - total_12sided_dice

    result = additional_dice
    return result

print(solution())