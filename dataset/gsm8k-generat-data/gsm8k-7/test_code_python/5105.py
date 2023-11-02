def solution():
    pine_tree_logs = 80
    maple_tree_logs = 60
    walnut_tree_logs = 100

    num_pine_trees = 8
    num_maple_trees = 3
    num_walnut_trees = 4

    # Calculate the total number of logs from all pine trees
    total_pine_logs = num_pine_trees * pine_tree_logs

    # Calculate the total number of logs from all maple trees
    total_maple_logs = num_maple_trees * maple_tree_logs

    # Calculate the total number of logs from all walnut trees
    total_walnut_logs = num_walnut_trees * walnut_tree_logs

    # Calculate the total number of logs
    total_logs = total_pine_logs + total_maple_logs + total_walnut_logs
    result = total_logs
    return result

print(solution())