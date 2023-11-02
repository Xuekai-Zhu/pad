def solution():
    """In mid-May, the depth of a river in Moreland is measured. By mid-June, the river is 10 feet deeper than mid-May. By mid-July, the river is three times deeper than mid-June. If the river is 45 feet deep in mid-July, how many feet deep was the river in mid-May?"""
    june_depth = (45 / 3) - 10
    may_depth = june_depth - 10
    result = may_depth
    return result

print(solution())