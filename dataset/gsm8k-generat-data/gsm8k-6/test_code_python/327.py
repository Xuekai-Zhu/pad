def solution():
    # Calculate the total number of baby minks Andy has
    baby_minks = 30 * 6  

    # Calculate the total number of minks Andy has after the babies are born
    total_minks = 30 + baby_minks  

    # Calculate the number of minks set free by activists
    free_minks = total_minks / 2  

    # Calculate the number of minks left for making coats
    minks_for_coats = total_minks - free_minks  

    # Calculate the number of coats Andy can make
    coats = minks_for_coats // 15  

    result = coats
    return result

print(solution())