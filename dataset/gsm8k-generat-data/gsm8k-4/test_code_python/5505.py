def solution():
    """There are 14 caterpillars on the tree. 4 more eggs hatch, and baby caterpillars climb out to munch on the leaves.  8 fat caterpillars leave the tree to cocoon themselves to be butterflies. How many caterpillars are left on the tree?"""
    # Define the initial number of caterpillars
    initial_caterpillars = 14

    # Calculate the number of caterpillars after the eggs hatch
    new_caterpillars = 4

    # Calculate the number of caterpillars after the fat ones leave
    fat_caterpillars = 8

    # Calculate the total number of caterpillars left on the tree
    remaining_caterpillars = initial_caterpillars + new_caterpillars - fat_caterpillars

    # return the result
    result = remaining_caterpillars
    return result

print(solution())