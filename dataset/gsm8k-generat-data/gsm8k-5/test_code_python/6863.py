def solution():
    logs_per_tree = 4  # Each tree produces 4 logs
    firewood_per_log = 5  # Each log produces 5 pieces of firewood
    total_firewood = 500  # The lumberjack has chopped 500 pieces of firewood

    # Calculate the total number of logs the lumberjack produced
    total_logs = total_firewood / firewood_per_log

    # Calculate the total number of trees the lumberjack chopped down
    total_trees = total_logs / logs_per_tree
    result = total_trees
    return result

print(solution())