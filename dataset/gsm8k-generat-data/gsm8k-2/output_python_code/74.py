def solution():
    """Four people lost a total of 103 kilograms of weight. The first person lost 27 kilograms. The second person lost 7 kilograms less than the first person. The two remaining people lost the same amount. How many kilograms did each of the last two people lose?"""
    total_loss = 103
    first_loss = 27
    second_loss = first_loss - 7
    remaining_loss = total_loss - first_loss - second_loss
    each_remaining_loss = remaining_loss / 2
    result = each_remaining_loss
    return result

print(solution())