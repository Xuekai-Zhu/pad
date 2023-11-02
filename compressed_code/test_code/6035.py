def solution():
    
    minks_bought = 30
    baby_minks = minks_bought * 6
    total_minks = minks_bought + baby_minks
    minks_set_free = total_minks / 2
    minks_for_coats = total_minks - minks_set_free
    coats = minks_for_coats // 15
    result = coats
    return result

print(solution())