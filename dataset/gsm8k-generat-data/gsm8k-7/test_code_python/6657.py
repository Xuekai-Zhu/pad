def solution():
    total_dice_needed = 14

    # Calculate Mark's number of 12-sided dice
    mark_num_dice = round(10 * 0.6)

    # Calculate James's number of 12-sided dice
    james_num_dice = round(8 * 0.75)

    # Calculate the total number of 12-sided dice the boys have
    total_num_dice = mark_num_dice + james_num_dice

    # Calculate the number of dice the boys need to buy
    num_dice_to_buy = total_dice_needed - total_num_dice
    result = num_dice_to_buy
    return result

print(solution())