def solution():
    """A lumberjack is chopping down trees so he can sell firewood. Each tree he chops produces 4 logs each, and each log is then chopped into 5 pieces of firewood. If the lumberjack has chopped 500 pieces of firewood, how many trees did he chop down?"""
    # Calculate the number of logs needed to produce 500 pieces of firewood
    logs_needed = 500 / 5

    # Calculate the number of trees needed to produce the required number of logs
    trees_needed = logs_needed / 4

    # Display the number of trees needed
    result = trees_needed
    return result

print(solution())