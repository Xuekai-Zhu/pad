def solution():
    """There are 48 crayons in the box.  Kiley takes 1/4 of them away.  Joe takes away half of the remaining crayons, how many crayons are left?"""
    # Define the initial number of crayons
    initial_count = 48

    # Calculate how many crayons Kiley takes away
    kiley_count = initial_count // 4

    # Calculate how many crayons are left after Kiley takes away hers
    remaining_count = initial_count - kiley_count

    # Calculate how many crayons Joe takes away
    joe_count = remaining_count // 2

    # Calculate the final count of crayons
    final_count = remaining_count - joe_count

    # Display the final count of crayons
    result = final_count
    return result

print(solution())