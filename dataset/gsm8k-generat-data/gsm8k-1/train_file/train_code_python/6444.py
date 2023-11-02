def solution():
    """Tina has 12 pink pens. She has 9 fewer green pens than pink pens. Tina has 3 more blue pens than green pens. How many pens does Tina have in total?"""
    pink_pens = 12
    green_pens = pink_pens - 9
    blue_pens = green_pens + 3
    total_pens = pink_pens + green_pens + blue_pens
    result = total_pens
    return result

print(solution())