def solution():
    """John and Yasmin's dad is named Gabriel. If John has twice the number of children that her sister has and Gabriel has six grandkids, how many children does Yasmin have?"""
    gabriel_grandkids = 6
    john_children = 4
    yasmin_children = (gabriel_grandkids - john_children) / 3
    result = yasmin_children
    return result

print(solution())