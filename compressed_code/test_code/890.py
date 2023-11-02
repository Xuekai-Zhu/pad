def solution():
    
    total_planks = 200
    storage_planks = total_planks // 4
    parents_planks = total_planks // 2
    friends_planks = 20
    bought_planks = total_planks - storage_planks - parents_planks - friends_planks
    result = bought_planks
    return result

print(solution())