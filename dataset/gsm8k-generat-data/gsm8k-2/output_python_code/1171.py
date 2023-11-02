def solution():
    """Colbert is building a treehouse out of wooden planks. The treehouse needs 200 wooden planks. A quarter of these planks come from Colbert’s storage, half of these planks come from Colbert’s parents, 20 planks come from Colbert’s friends and he buys the rest from the store. How many planks of wood does he need to buy from the store to finish his treehouse?"""
    total_planks = 200
    storage_planks = total_planks // 4
    parents_planks = total_planks // 2
    friends_planks = 20
    bought_planks = total_planks - storage_planks - parents_planks - friends_planks
    result = bought_planks
    return result

print(solution())