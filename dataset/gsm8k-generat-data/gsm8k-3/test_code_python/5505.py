def solution():
    """There are 14 caterpillars on the tree. 4 more eggs hatch, and baby caterpillars climb out to munch on the leaves.  8 fat caterpillars leave the tree to cocoon themselves to be butterflies.  How many caterpillars are left on the tree?"""
    # Define the initial number of caterpillars
    initial_caterpillars = 14

    # Define the number of eggs that hatch and the number of caterpillars that leave
    new_caterpillars = 4
    leaving_caterpillars = 8

    # Calculate the final number of caterpillars on the tree
    final_caterpillars = initial_caterpillars + new_caterpillars - leaving_caterpillars

    # Display the final number of caterpillars
    result = final_caterpillars
    return result

print(solution())