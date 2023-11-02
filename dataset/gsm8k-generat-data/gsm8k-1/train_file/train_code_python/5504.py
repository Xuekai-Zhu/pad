def solution():
    """There are 14 caterpillars on the tree. 4 more eggs hatch, and baby caterpillars climb out to munch on the leaves. 8 fat caterpillars leave the tree to cocoon themselves to be butterflies. How many caterpillars are left on the tree?"""
    starting_caterpillars = 14
    hatched_caterpillars = 4
    leaving_caterpillars = 8
    remaining_caterpillars = starting_caterpillars + hatched_caterpillars - leaving_caterpillars
    result = remaining_caterpillars
    return result

print(solution())