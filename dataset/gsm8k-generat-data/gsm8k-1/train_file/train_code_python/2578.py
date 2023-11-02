def solution():
    """Nori had 4 boxes of crayons with 8 crayons in each box. She gave 5 crayons to Mae and also give some crayons to Lea. How many more crayons did she give to Lea than Mae if she has only 15 crayons left?"""
    total_crayons = 4 * 8
    crayons_given_to_mae = 5
    crayons_left_after_mae = total_crayons - crayons_given_to_mae
    crayons_given_to_lea = total_crayons - 15 - crayons_left_after_mae
    difference = crayons_given_to_lea - crayons_given_to_mae
    result = difference
    return result

print(solution())