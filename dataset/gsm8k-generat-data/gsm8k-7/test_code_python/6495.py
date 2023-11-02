def solution():
    pieces_per_tree = 75
    logs_per_day = 5
    num_days = 120  # Nov 1 to Feb 28

    # Calculate the total number of logs Bart will burn during the 120 days
    total_logs_burned = logs_per_day * num_days

    # Calculate the total number of trees Bart will need to cut down to get enough firewood
    total_trees = total_logs_burned / pieces_per_tree
    result = total_trees
    return result

print(solution())