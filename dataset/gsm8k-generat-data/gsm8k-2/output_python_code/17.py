def solution():
    """In a truck, there are 26 pink hard hats, 15 green hard hats, and 24 yellow hard hats. If Carl takes away 4
    pink hard hats, and John takes away 6 pink hard hats and twice as many green hard hats as the number of pink 
    hard hats that he removed, then calculate the total number of hard hats that remained in the truck."""
    num_pink = 26
    num_green = 15
    num_yellow = 24
    
    # Carl takes away 4 pink hard hats
    num_pink -= 4
    
    # John takes away 6 pink hard hats and twice as many green hard hats
    num_pink -= 6
    num_green -= 2 * 6
    
    # Calculate the total number of hard hats that remained in the truck
    total_hard_hats = num_pink + num_green + num_yellow
    
    result = total_hard_hats
    return result

print(solution())