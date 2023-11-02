def solution():
    """Will catches 16 catfish and 10 eels. Henry challenges himself to catch 3 trout for every catfish Will catches. Due to environmental concerns, Henry decides to return half his catch after meeting his own challenge. How many fishes do they have altogether now?"""
    catfish = 16
    eels = 10
    trout = 3 * catfish
    total_fish = catfish + eels + trout
    half_trout = trout / 2
    total_fish_after_return = catfish + eels + half_trout
    result = total_fish_after_return
    return result

print(solution())