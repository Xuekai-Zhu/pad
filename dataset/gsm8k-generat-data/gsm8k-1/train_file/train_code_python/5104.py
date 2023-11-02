def solution():
    """Jerry is cutting up wood for his wood-burning stove. Each pine tree makes 80 logs, each maple tree makes 60 logs, and each walnut tree makes 100 logs. If Jerry cuts up 8 pine trees, 3 maple trees, and 4 walnut trees, how many logs does he get?"""
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