def solution():
    
    jane_shadow = 0.5
    tree_shadow = 10
    jane_height = 1.5
    tree_height = (tree_shadow / jane_shadow) * jane_height
    result = tree_height
    return result

print(solution())