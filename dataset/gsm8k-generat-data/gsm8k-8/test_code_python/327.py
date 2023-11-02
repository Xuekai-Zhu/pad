def solution():
    # Calculate the total number of minks after they have babies
    total_minks = 30 + (30*6)

    # Calculate the number of minks set free by activists
    minks_set_free = total_minks / 2

    # Calculate the number of minks left for Andy
    minks_left = total_minks - minks_set_free

    # Calculate the number of coats Andy can make
    coats = minks_left // 15
    result = coats
    return result

print(solution())