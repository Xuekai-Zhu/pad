def solution():
    total_crayons = 48  # There are 48 crayons in the box
    taken_by_kiley = total_crayons / 4  # Kiley takes away 1/4 of the crayons
    remaining_crayons = total_crayons - taken_by_kiley  # Calculate the number of remaining crayons
    taken_by_joe = remaining_crayons / 2  # Joe takes away half of the remaining crayons
    remaining_crayons -= taken_by_joe  # Subtract the number of crayons taken by Joe from the remaining crayons

    result = remaining_crayons
    return result

print(solution())