def solution():
    """Tina has 12 pink pens. She has 9 fewer green pens than pink pens. Tina has 3 more blue pens than green pens. How many pens does Tina have in total?"""
    # Define the number of pink pens
    pink_pens = 12

    # Calculate the number of green pens
    green_pens = pink_pens - 9

    # Calculate the number of blue pens
    blue_pens = green_pens + 3

    # Calculate the total number of pens
    total_pens = pink_pens + green_pens + blue_pens

    # return the result
    result = total_pens
    return result

print(solution())