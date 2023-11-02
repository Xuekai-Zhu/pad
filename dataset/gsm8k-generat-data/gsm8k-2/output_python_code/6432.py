def solution():
    """There are 48 crayons in the box. Kiley takes 1/4 of them away. Joe takes away half of the remaining crayons, how many crayons are left?"""
    total_crayons = 48
    kiley_crayons = total_crayons * 0.25
    remaining_crayons = total_crayons - kiley_crayons
    joe_crayons = remaining_crayons * 0.5
    final_crayons = remaining_crayons - joe_crayons
    result = final_crayons
    return result

print(solution())