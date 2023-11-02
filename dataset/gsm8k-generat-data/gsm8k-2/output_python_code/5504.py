def solution():
    """There are 14 caterpillars on the tree. 4 more eggs hatch, and baby caterpillars climb out to munch on the leaves. 8 fat caterpillars leave the tree to cocoon themselves to be butterflies. How many caterpillars are left on the tree?"""
    initial_caterpillars = 14
    new_caterpillars = 4
    leaving_caterpillars = 8
    total_caterpillars = initial_caterpillars + new_caterpillars - leaving_caterpillars
    result = total_caterpillars
    return result

print(solution())