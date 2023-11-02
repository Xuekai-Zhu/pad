def solution():
    pieces_of_firewood = 500
    logs_per_tree = 4
    pieces_of_firewood_per_log = 5
    total_logs = pieces_of_firewood / pieces_of_firewood_per_log
    total_trees = total_logs / logs_per_tree
    result = total_trees
    return result

print(solution())