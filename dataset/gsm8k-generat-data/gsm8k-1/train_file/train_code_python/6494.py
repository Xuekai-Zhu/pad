def solution():
    """Every tree that Bart cuts down gives him 75 pieces of firewood. If he burns 5 logs a day from November 1 through February 28, how many trees will he need to cut down?"""
    pieces_per_tree = 75
    days_burning = 120 # November 1 to February 28 is 120 days
    daily_logs_burned = 5
    total_logs_burned = days_burning * daily_logs_burned
    trees_needed = total_logs_burned / pieces_per_tree
    result = trees_needed
    return result

print(solution())