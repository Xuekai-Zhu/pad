def solution():
    """Tim grows 5 trees. Each year he collects 6 lemons from each tree. How many lemons does he get in a decade?"""
    trees = 5
    lemons_per_tree_per_year = 6
    years = 10
    total_lemons = trees * lemons_per_tree_per_year * years
    result = total_lemons
    return result

print(solution())