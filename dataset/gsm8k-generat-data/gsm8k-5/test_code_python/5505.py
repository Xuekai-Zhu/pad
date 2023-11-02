def solution():
    initial_caterpillars = 14  # There are 14 caterpillars on the tree
    hatched_caterpillars = 4  # 4 more caterpillars hatch
    leaving_caterpillars = 8  # 8 caterpillars leave to cocoon themselves

    # Calculate the remaining caterpillars on the tree
    remaining_caterpillars = initial_caterpillars + hatched_caterpillars - leaving_caterpillars
    result = remaining_caterpillars
    return result

print(solution())