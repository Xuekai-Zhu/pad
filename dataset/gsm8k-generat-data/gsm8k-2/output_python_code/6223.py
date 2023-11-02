def solution():
    """Eliza has 4 siblings. The total height of all 5 siblings combined is 330 inches. Two of her siblings are both 66 inches tall. Another sibling is 60 inches tall. If Eliza is 2 inches shorter than the last sibling, how tall is Eliza?"""
    total_height = 330
    height_66 = 66
    height_60 = 60
    height_last = (total_height - height_66 - height_66 - height_60) / 2
    eliza_height = height_last - 2
    result = eliza_height
    return result

print(solution())