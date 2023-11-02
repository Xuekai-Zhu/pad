def solution():
    """Colbert is building a treehouse out of wooden planks. The treehouse needs 200 wooden planks. A quarter of these planks come from Colbert’s storage, half of these planks come from Colbert’s parents, 20 planks come from Colbert’s friends and he buys the rest from the store. How many planks of wood does he need to buy from the store to finish his treehouse?"""
    # Define the total number of wooden planks needed
    total_planks = 200

    # Calculate the number of wooden planks coming from storage
    storage_planks = total_planks // 4

    # Calculate the number of wooden planks coming from Colbert's parents
    parents_planks = (total_planks - storage_planks) // 2

    # Calculate the number of wooden planks coming from Colbert's friends
    friends_planks = 20

    # Calculate the number of wooden planks needed to be bought from the store
    store_planks = total_planks - storage_planks - parents_planks - friends_planks

    # Display the number of planks needed to be bought from the store
    result = store_planks
    return result

print(solution())