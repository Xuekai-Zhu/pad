def solution():
    logs_per_tree = 4
    pieces_per_log = 5
    total_pieces = 500

    # Calculate the total number of logs chopped
    total_logs = total_pieces / pieces_per_log

    # Calculate the total number of trees chopped
    total_trees = total_logs / logs_per_tree
    result = total_trees
    return result

print(solution())