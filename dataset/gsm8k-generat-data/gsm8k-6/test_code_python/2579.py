def solution():
    # Calculate the total number of crayons Nori had
    total_crayons = 4 * 8  # 4 boxes of crayons with 8 crayons in each box

    # Calculate the number of crayons Nori gave to Mae
    mae_crayons = 5

    # Calculate the number of crayons Nori gave to Lea
    lea_crayons = total_crayons - mae_crayons - 15

    # Calculate the difference between the number of crayons given to Mae and Lea
    diff_crayons = lea_crayons - mae_crayons

    result = diff_crayons
    return result

print(solution())