def solution():
    
    bracelets = 3
    necklace = 2
    mug = 1
    cost = (bracelets * 15) + (necklace * 10) + (mug * 20)
    change = 100 - cost
    result = change
    return result

print(solution())