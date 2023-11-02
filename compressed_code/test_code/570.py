def solution():
    
    initial_pick = 250
    fresh_ratio = 0.6
    fresh_pick = initial_pick * fresh_ratio
    small_throwaway = 15
    final_pick = fresh_pick - small_throwaway
    result = final_pick
    return result

print(solution())