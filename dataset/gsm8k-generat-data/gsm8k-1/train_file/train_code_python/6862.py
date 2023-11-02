def solution():
    """A lumberjack is chopping down trees so he can sell firewood. Each tree he chops produces 4 logs each, and each log is then chopped into 5 pieces of firewood.
    If the lumberjack has chopped 500 pieces of firewood, how many trees did he chop down?"""
    logs_per_tree = 4
    firewood_per_log = 5
    total_firewood = 500
    logs_needed = total_firewood / firewood_per_log
    trees_chopped = logs_needed / logs_per_tree
    result = trees_chopped
    return result

print(solution())