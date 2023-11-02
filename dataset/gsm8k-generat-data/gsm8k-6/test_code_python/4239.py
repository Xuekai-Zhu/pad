def solution():
    # Calculate the total number of burgers Alex needs to cook
    total_burgers = 3 * 9  # 1 friend is bringing their own food, so only 9 guests need burgers
    burgers_without_buns = total_burgers - 9  # 1 friend doesn't eat bread, so no buns needed for their burgers
    total_buns = burgers_without_buns * 2  # 2 buns needed for each burger

    # Calculate the number of packs of buns Alex needs to buy
    packs_of_buns = total_buns // 8 + (total_buns % 8 > 0)  # round up to the nearest pack
    result = packs_of_buns
    return result

print(solution())