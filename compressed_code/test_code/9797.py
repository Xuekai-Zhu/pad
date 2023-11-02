def solution():
    
    logs_per_pine_tree = 80
    logs_per_maple_tree = 60
    logs_per_walnut_tree = 100
    pine_trees = 8
    maple_trees = 3
    walnut_trees = 4
    total_logs = (logs_per_pine_tree * pine_trees) + (logs_per_maple_tree * maple_trees) + (logs_per_walnut_tree * walnut_trees)
    result = total_logs
    return result

print(solution())