def solution():
    """Colbert is building a treehouse out of wooden planks. The treehouse needs 200 wooden planks. A quarter of these planks come from Colbert’s storage, half of these planks come from Colbert’s parents, 20 planks come from Colbert’s friends and he buys the rest from the store. How many planks of wood does he need to buy from the store to finish his treehouse?"""
    # Define the total number of planks needed
    total_planks = 200

    # Calculate the number of planks from Colbert's storage
    storage_planks = total_planks / 4

    # Calculate the number of planks from Colbert's parents
    parents_planks = total_planks / 2

    # Calculate the number of planks from Colbert's friends
    friends_planks = 20

    # Calculate the total number of planks from sources other than the store
    nonstore_planks = storage_planks + parents_planks + friends_planks

    # Calculate the number of planks that Colbert needs to buy from the store
    store_planks = total_planks - nonstore_planks

    # Return the result
    result = store_planks
    return result

print(solution())