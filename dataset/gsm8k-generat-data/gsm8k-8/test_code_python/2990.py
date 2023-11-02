def solution():
    # Let x be the original number of jewels owned by the dragon
    x = 3 * 2

    # The dragon now has 2x jewels, which is a third of the original amount
    # 2x = x/3, so x = 6
    x = 6

    # The dragon now has 2x jewels, which is 12
    jewels_owned = 2 * x
    
    result = jewels_owned
    return result

print(solution())