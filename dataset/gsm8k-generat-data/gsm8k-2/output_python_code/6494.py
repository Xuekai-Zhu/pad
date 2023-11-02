def solution():
    """Every tree that Bart cuts down gives him 75 pieces of firewood. If he burns 5 logs a day from November 1 through February 28, how many trees will he need to cut down?"""
    logs_per_tree = 75
    start_date = "November 1"
    end_date = "February 28"
    days = (datetime.datetime.strptime(end_date, "%B %d") - datetime.datetime.strptime(start_date, "%B %d")).days
    total_logs_needed = 5 * days
    trees_needed = math.ceil(total_logs_needed / logs_per_tree)
    result = trees_needed
    return result

print(solution())