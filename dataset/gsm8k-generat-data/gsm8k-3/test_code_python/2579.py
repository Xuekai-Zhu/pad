def solution():
    """Nori had 4 boxes of crayons with 8 crayons in each box. She gave 5 crayons to Mae and also gave some crayons to Lea. How many more crayons did she give to Lea than Mae if she has only 15 crayons left?"""
    # Define the initial number of crayons Nori had
    initial_crayons = 4 * 8

    # Calculate the number of crayons Nori gave to Mae
    mae_crayons = 5

    # Calculate the number of crayons Nori gave to Lea
    lea_crayons = initial_crayons - mae_crayons - 15

    # Calculate the difference between the number of crayons Nori gave to Lea and Mae
    difference = lea_crayons - mae_crayons

    # Display the difference
    result = difference
    return result

print(solution())