def solution():
    time_to_pick = 2
    time_to_make_syrup = 3
    quarts_of_syrup = 9
    cherries_per_quart = 500
    total_cherries = quarts_of_syrup * cherries_per_quart
    time_to_make_9_quarts = (total_cherries / 300) * time_to_pick + time_to_make_syrup
    result = time_to_make_9_quarts
    return result

print(solution())