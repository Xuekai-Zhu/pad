def solution():
    
    catfish = 16
    eels = 10
    trout = 3 * catfish
    total_fish = catfish + eels + trout
    half_trout = trout / 2
    total_fish_after_return = catfish + eels + half_trout
    result = total_fish_after_return
    return result

print(solution())