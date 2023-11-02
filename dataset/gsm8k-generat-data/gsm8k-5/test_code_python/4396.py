def solution():
    trees_per_square_mile = 600  # Each square mile of forest has 600 trees
    area_of_forest = 4 * 6  # The forest is a rectangle measuring 4 miles by 6 miles
    total_trees = area_of_forest * trees_per_square_mile  # Calculate the total number of trees in the forest
    loggers_per_day = 6  # One logger can cut down 6 trees per day
    days_per_month = 30  # There are 30 days in each month
    loggers = 8  # There are 8 loggers working together

    # Calculate the total number of days it will take the loggers to cut down all the trees
    total_days = total_trees / (loggers * loggers_per_day)

    # Calculate the number of months it will take the loggers to cut down all the trees
    months = total_days / days_per_month
    result = months
    return result

print(solution())