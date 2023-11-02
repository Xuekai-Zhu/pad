def solution():
    # Calculate the total height of Eliza's siblings without herself
    total_height = 330 - 66 - 66 - 60  

    # Calculate the height of Eliza by subtracting her siblings' total height from the total height of all 5 siblings
    height_Eliza = total_height - (2 + 60)

    # Subtract 2 inches from the height of the last sibling to get Eliza's height
    height_Eliza -= 2  
    result = height_Eliza
    return result

print(solution())