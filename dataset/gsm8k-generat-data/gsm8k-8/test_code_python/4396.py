def solution():
    # Calculate the total number of trees in the forest
    total_area = 4 * 6
    num_trees_per_square_mile = 600
    total_trees = total_area * num_trees_per_square_mile

    # Calculate the total number of trees that can be cut down per day
    num_trees_per_day = 6 * 1

    # Calculate the total number of trees that can be cut down in one month
    num_days_per_month = 30
    num_trees_per_month = num_trees_per_day * num_days_per_month * 8

    # Calculate the total number of months it will take to cut down all the trees
    num_months = total_trees / num_trees_per_month
    result = num_months
    return result

print(solution())