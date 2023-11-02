def solution():
    carlos_children = 11
    helio_children = 9
    bakers_dozen = 13
    total_children = carlos_children + helio_children
    if total_children >= bakers_dozen:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())