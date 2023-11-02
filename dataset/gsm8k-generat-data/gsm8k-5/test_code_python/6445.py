def solution():
    pink_pens = 12  # Tina has 12 pink pens
    green_pens = pink_pens - 9  # Tina has 9 fewer green pens than pink pens
    blue_pens = green_pens + 3  # Tina has 3 more blue pens than green pens

    # Calculate the total number of pens Tina has
    total_pens = pink_pens + green_pens + blue_pens
    result = total_pens
    return result

print(solution())