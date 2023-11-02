def solution():
    """There are 48 crayons in the box. Kiley takes 1/4 of them away. Joe takes away half of the remaining crayons, how many crayons are left?"""
    # Define the initial number of crayons
    initial_crayons = 48

    # Kiley takes away 1/4 of the crayons
    kiley_crayons = initial_crayons * (1/4)

    # Calculate the remaining crayons
    remaining_crayons = initial_crayons - kiley_crayons

    # Joe takes away half of the remaining crayons
    joe_crayons = remaining_crayons * (1/2)

    # Calculate the final number of crayons
    final_crayons = remaining_crayons - joe_crayons

    # return the result
    result = final_crayons
    return result

print(solution())