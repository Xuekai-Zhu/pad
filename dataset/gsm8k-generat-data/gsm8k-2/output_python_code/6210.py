def solution():
    """Jane is looking at a tree. At the same time, the tree and Jane are casting shadows - the tree of 10 meters and Jane of 0.5 meters. Jane is 1.5 meters tall. How tall is the tree?"""
    jane_shadow = 0.5
    tree_shadow = 10
    jane_height = 1.5
    tree_height = (tree_shadow / jane_shadow) * jane_height
    result = tree_height
    return result

print(solution())