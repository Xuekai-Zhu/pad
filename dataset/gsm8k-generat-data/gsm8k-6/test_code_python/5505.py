def solution():
    # Calculate the total number of caterpillars remaining on the tree
    initial_caterpillars = 14
    new_caterpillars = 4
    leaving_caterpillars = 8
    remaining_caterpillars = initial_caterpillars + new_caterpillars - leaving_caterpillars
    result = remaining_caterpillars
    return result

print(solution())