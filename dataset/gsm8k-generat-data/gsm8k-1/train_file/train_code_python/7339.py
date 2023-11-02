def solution():
    """John and Yasmin's dad is named Gabriel. If John has twice the number of children that her sister has and Gabriel has six grandkids, how many children does Yasmin have?"""
    gabriel_grandkids = 6
    john_children = 4 #(twice the number of Yasmin's children, so she has 2)
    yasmin_children = gabriel_grandkids - john_children
    result = yasmin_children
    return result

print(solution())