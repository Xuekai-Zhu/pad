def solution():
    """Will catches 16 catfish and 10 eels. Henry challenges himself to catch 3 trout for every catfish Will catches. Due to environmental concerns, Henry decides to return half his catch after meeting his own challenge. How many fishes do they have altogether now?"""
    will_catfish = 16
    will_eels = 10
    henry_trout_per_catfish = 3
    henry_trout = will_catfish * henry_trout_per_catfish
    total_fish = will_catfish + will_eels + henry_trout
    half_henry_trout = henry_trout / 2
    total_fish -= half_henry_trout
    result = total_fish
    return result

print(solution())