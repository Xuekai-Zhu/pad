def solution():
    # Calculate the total number of crayons Nori had
    total_crayons = 4 * 8

    # Calculate the number of crayons Nori gave to Mae
    mae_crayons = 5

    # Calculate the remaining number of crayons after giving some to Mae
    remaining_crayons = 15

    # Calculate the number of crayons Nori gave to Lea
    lea_crayons = remaining_crayons - mae_crayons

    # Calculate the difference in crayons Nori gave to Lea and Mae
    difference = lea_crayons - mae_crayons
    result = difference
    return result

print(solution())