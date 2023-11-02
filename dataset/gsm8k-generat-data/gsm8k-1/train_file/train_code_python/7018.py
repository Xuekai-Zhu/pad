def solution():
    """One and a half increase in the productivity in Tutuwanas saw-mill this year was due to the Albaszu machine's being finally repaired. If the Albaszu machine was cutting 10 trees daily, how many trees is it cutting now after its improvement?"""
    initial_trees_cut = 10
    increase_percent = 150
    new_trees_cut = initial_trees_cut * (1 + (increase_percent / 100))
    result = new_trees_cut
    return result

print(solution())