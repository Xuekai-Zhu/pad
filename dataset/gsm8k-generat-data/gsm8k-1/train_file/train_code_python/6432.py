def solution():
    """There are 48 crayons in the box. Kiley takes 1/4 of them away. Joe takes away half of the remaining crayons, how many crayons are left?"""
    total_crayons = 48
    kiley_taken = total_crayons / 4
    remaining_crayons = total_crayons - kiley_taken
    joe_taken = remaining_crayons / 2
    crayons_left = remaining_crayons - joe_taken
    result = crayons_left
    return result

print(solution())