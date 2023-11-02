def solution():
    # Calculate the number of planks coming from Colbert's storage
    storage_planks = 200 / 4

    # Calculate the number of planks coming from Colbert's parents
    parents_planks = 200 / 2

    # Calculate the total planks from all sources except store
    total = storage_planks + parents_planks + 20

    # Calculate the number of planks needed to buy from the store
    to_buy = 200 - total
    result = to_buy
    return result

print(solution())