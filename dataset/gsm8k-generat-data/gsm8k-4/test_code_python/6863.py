def solution():
    """A lumberjack is chopping down trees so he can sell firewood. Each tree he chops produces 4 logs each, and each log is then chopped into 5 pieces of firewood. If the lumberjack has chopped 500 pieces of firewood, how many trees did he chop down?"""
    # Define the number of logs produced from each tree and the number of pieces of firewood produced from each log
    LOGS_PER_TREE = 4
    FIREWOOD_PER_LOG = 5

    # Calculate the total number of logs produced
    total_logs = 500 / FIREWOOD_PER_LOG

    # Calculate the number of trees needed to produce that many logs
    trees_chopped = total_logs / LOGS_PER_TREE

    # Round up to the nearest integer since the lumberjack can't chop a partial tree
    trees_chopped = int(trees_chopped) + 1

    # Return the result
    result = trees_chopped
    return result

print(solution())