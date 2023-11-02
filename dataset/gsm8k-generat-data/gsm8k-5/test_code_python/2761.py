def solution():
    catfish = 16
    eels = 10
    trout = 3 * catfish  # Henry caught 3 trout for every catfish Will caught
    total_fish = catfish + eels + trout
    henry_returned = trout / 2  # Henry returned half of the trout he caught
    total_fish_now = total_fish - henry_returned
    result = total_fish_now
    return result

print(solution())