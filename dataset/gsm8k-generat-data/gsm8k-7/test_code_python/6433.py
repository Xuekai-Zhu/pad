def solution():
    num_crayons = 48
    kiley_fraction = 1/4
    joe_fraction = 1/2

    # Calculate the number of crayons Kiley takes away
    kiley_crayons = num_crayons * kiley_fraction

    # Calculate the number of crayons remaining after Kiley takes away her share
    remaining_crayons = num_crayons - kiley_crayons

    # Calculate the number of crayons Joe takes away
    joe_crayons = remaining_crayons * joe_fraction

    # Calculate the number of crayons remaining after Joe takes away his share
    total_remaining = remaining_crayons - joe_crayons
    result = total_remaining
    return result

print(solution())