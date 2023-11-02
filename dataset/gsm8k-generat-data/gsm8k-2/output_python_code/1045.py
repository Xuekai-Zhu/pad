def solution():
    """Susan had a bouquet of 3 dozen roses. She gave half to her daughter, and then placed the rest in a vase. The next day, one-third of the flowers in the vase were wilted. After removing the wilted flowers, how many flowers remained in the vase?"""
    total_roses = 3 * 12
    roses_given_away = total_roses / 2
    roses_in_vase = total_roses - roses_given_away
    wilted_roses = roses_in_vase / 3
    remaining_roses = roses_in_vase - wilted_roses
    result = remaining_roses
    return result

print(solution())