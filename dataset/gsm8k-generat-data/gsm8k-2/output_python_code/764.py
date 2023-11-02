def solution():
    """Brenda picks 250 peaches. When she sorts through them, only 60% are fresh, and Brenda has to throw 15 away for being too small. How many peaches does Brenda have left?"""
    initial_pick = 250
    fresh_ratio = 0.6
    fresh_pick = initial_pick * fresh_ratio
    small_throwaway = 15
    final_pick = fresh_pick - small_throwaway
    result = final_pick
    return result

print(solution())