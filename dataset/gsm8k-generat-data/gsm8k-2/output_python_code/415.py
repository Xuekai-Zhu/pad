def solution():
    """In mid-May, the river flowing through Moreland is five feet deep. By mid-June, the river is 10 feet deeper than mid-May. By mid-July, the river is three times deeper than mid-June. How many feet deep is the river by mid-July?"""
    may_depth = 5
    june_depth = may_depth + 10
    july_depth = 3 * june_depth
    result = july_depth
    return result

print(solution())