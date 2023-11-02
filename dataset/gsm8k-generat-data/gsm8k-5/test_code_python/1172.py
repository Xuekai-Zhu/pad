def solution():
    total_planks = 200  # The treehouse needs 200 wooden planks
    planks_from_storage = total_planks / 4  # A quarter of the planks come from Colbert's storage
    planks_from_parents = total_planks / 2  # Half of the planks come from Colbert's parents
    planks_from_friends = 20  # 20 planks come from Colbert's friends
    planks_bought = total_planks - planks_from_storage - planks_from_parents - planks_from_friends

    result = planks_bought
    return result

print(solution())