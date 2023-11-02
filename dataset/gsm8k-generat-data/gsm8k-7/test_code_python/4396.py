def solution():
    num_loggers = 8
    logger_productivity = 6 #trees per day
    forest_area = 4 * 6 #square miles
    tree_density = 600 #trees per square mile
    total_trees = forest_area * tree_density

    # Calculate the total number of days needed to cut down all the trees
    total_days = total_trees / (num_loggers * logger_productivity)

    # Calculate the number of months needed to cut down all the trees
    num_months = total_days / 30

    result = num_months
    return result

print(solution())