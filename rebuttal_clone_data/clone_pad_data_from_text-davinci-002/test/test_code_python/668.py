def solution():
    total_planks = 200
    planks_from_storage = total_planks * 0.25
    planks_from_parents = total_planks * 0.50
    planks_from_friends = 20
    planks_from_store = total_planks - planks_from_storage - planks_from_parents - planks_from_friends
    result = planks_from_store
    return result

print(solution())