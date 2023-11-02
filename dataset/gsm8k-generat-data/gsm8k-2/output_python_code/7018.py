def solution():
    """One and a half increase in the productivity in Tutuwanas saw-mill this year was due to the Albaszu machine's being finally repaired. If the Albaszu machine was cutting 10 trees daily, how many trees is it cutting now after its improvement?"""
    starting_trees_per_day = 10
    productivity_increase = 1.5
    new_trees_per_day = starting_trees_per_day * productivity_increase
    result = new_trees_per_day
    return result

print(solution())