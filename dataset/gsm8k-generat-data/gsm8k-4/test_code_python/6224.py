def solution():
    """Eliza has 4 siblings. The total height of all 5 siblings combined is 330 inches. Two of her siblings are both 66 inches tall. Another sibling is 60 inches tall. If Eliza is 2 inches shorter than the last sibling, how tall is Eliza?"""
    # Define the total height of all siblings except Eliza
    total_siblings_height = 66*2 + 60

    # Calculate Eliza's height
    eliza_height = (330 - total_siblings_height) - 2

    # Return the result
    result = eliza_height
    return result

print(solution())