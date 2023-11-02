def solution():
    
    total_planks = 200
    storage_planks = total_planks / 4
    parent_planks = total_planks / 2
    friend_planks = 20
    bought_planks = total_planks - storage_planks - parent_planks - friend_planks
    result = bought_planks
    return result

print(solution())