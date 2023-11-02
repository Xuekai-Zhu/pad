def solution():
    """A lumberjack is chopping down trees so he can sell firewood. Each tree he chops produces 4 logs each, and each log is then chopped into 5 pieces of firewood. If the lumberjack has chopped 500 pieces of firewood, how many trees did he chop down?"""
    pieces_per_log = 5
    logs_per_tree = 4
    total_pieces = 500
    pieces_per_tree = logs_per_tree * pieces_per_log
    trees_chopped = total_pieces / pieces_per_tree
    result = trees_chopped
    return result

print(solution())