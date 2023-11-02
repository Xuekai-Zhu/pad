def solution():
    roses = 3 * 12  # Susan had a bouquet of 3 dozen roses
    roses_given_away = roses // 2  # Susan gave half of the roses to her daughter
    roses_remaining = roses - roses_given_away  # Susan has the remaining roses in the vase
    wilted_roses = roses_remaining // 3  # One-third of the flowers in the vase were wilted
    remaining_roses = roses_remaining - wilted_roses  # Susan removed the wilted flowers

    result = remaining_roses
    return result

print(solution())