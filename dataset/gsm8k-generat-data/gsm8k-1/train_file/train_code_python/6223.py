def solution():
    """Eliza has 4 siblings. The total height of all 5 siblings combined is 330 inches. Two of her siblings are both 66 inches tall. Another sibling is 60 inches tall. If Eliza is 2 inches shorter than the last sibling, how tall is Eliza?"""
    total_height = 330
    sibling_1 = 66
    sibling_2 = 66
    sibling_3 = 60
    sibling_5 = (total_height - sibling_1 - sibling_2 - sibling_3) / 2
    eliza = sibling_5 - 2
    result = eliza
    return result

print(solution())