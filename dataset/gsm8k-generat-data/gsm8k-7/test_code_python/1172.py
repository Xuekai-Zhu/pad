def solution():
    total_planks = 200
    storage_planks = total_planks / 4
    parents_planks = total_planks / 2
    friends_planks = 20

    # Calculate how many planks of wood Colbert already has
    total_planks_owned = storage_planks + parents_planks + friends_planks

    # Calculate how many planks of wood Colbert still needs to buy
    remaining_planks = total_planks - total_planks_owned
    result = remaining_planks
    return result

print(solution())