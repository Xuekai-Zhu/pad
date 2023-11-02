def solution():
    # Calculate the number of planks from Colbert's storage
    storage_planks = 200 / 4

    # Calculate the number of planks from Colbert's parents
    parent_planks = 200 / 2

    # Calculate the total number of planks from storage and parents
    total_planks = storage_planks + parent_planks + 20

    # Calculate the number of planks needed to be bought from the store
    store_planks = 200 - total_planks
    result = store_planks
    return result

print(solution())