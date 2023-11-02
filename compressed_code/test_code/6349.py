def solution():
    
    henry_seashells = 11
    paul_seashells = 24
    initial_total = 59
    leo_seashells = initial_total - henry_seashells - paul_seashells
    leo_gives = leo_seashells / 4
    total_now = initial_total - leo_gives
    result = total_now
    return result

print(solution())