def solution():
    # Calculate the total number of legos Bob needs to build the pyramid
    level1_legos = 7*7
    level2_legos = 6*6
    level3_legos = 5*5
    total_legos = level1_legos + level2_legos + level3_legos
    result = total_legos
    return result

print(solution())