def solution():
    """Nori had 4 boxes of crayons with 8 crayons in each box. She gave 5 crayons to Mae and also give some crayons to Lea. How many more crayons did she give to Lea than Mae if she has only 15 crayons left?"""
    # Define the initial number of crayons
    initial_crayons = 4 * 8

    # Subtract the crayons given to Mae
    crayons_left = initial_crayons - 5

    # Subtract the remaining crayons to get the number given to Lea
    crayons_to_lea = crayons_left - 15

    # Calculate the difference between crayons given to Lea and Mae
    difference = crayons_to_lea - 5

    # return the result
    result = difference
    return result

print(solution())