def solution():
    """Nori had 4 boxes of crayons with 8 crayons in each box. She gave 5 crayons to Mae and also give some crayons to Lea. How many more crayons did she give to Lea than Mae if she has only 15 crayons left?"""
    total_crayons = 4 * 8
    total_crayons -= 5  # gave 5 to Mae
    remaining_crayons = 15  # left after giving some to Lea
    lea_crayons = total_crayons - remaining_crayons
    mae_crayons = 5  # initially gave 5 to Mae
    difference = lea_crayons - mae_crayons
    result = difference
    return result

print(solution())