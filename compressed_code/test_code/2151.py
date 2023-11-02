def solution():
    
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