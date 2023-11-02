def solution():
    # Calculate the total number of crayons Nori had
    total_crayons = 4 * 8  # 4 boxes of crayons with 8 crayons in each box

    # Calculate the number of crayons Nori gave to Mae
    crayons_to_mae = 5

    # Calculate the number of crayons Nori gave to Lea
    crayons_to_lea = total_crayons - crayons_to_mae - 15  # Nori has 15 crayons left

    # Calculate the difference in the number of crayons Nori gave to Lea and Mae
    difference = crayons_to_lea - crayons_to_mae
    result = difference
    return result

print(solution())