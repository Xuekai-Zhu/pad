def solution():
    # Define the initial number of fish
    guppies = 94
    angelfish = 76
    tiger_sharks = 89 
    oscar_fish = 58 

    # Subtract the number of fish sold
    guppies -= 30 
    angelfish -= 48 
    tiger_sharks -= 17 
    oscar_fish -= 24 

    # Calculate the total number of fish remaining
    total_fish_remaining = guppies + angelfish + tiger_sharks + oscar_fish 

    result = total_fish_remaining
    return result

print(solution())