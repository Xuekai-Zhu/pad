def solution():
    # Calculate the total number of trees in the forest
    total_trees = 4 * 6 * 600  # area of the rectangle multiplied by the number of trees per square mile

    # Calculate the total number of trees cut down by 8 loggers in one day
    trees_cut_in_one_day = 8 * 6  # 8 loggers each cut down 6 trees per day

    # Calculate the total number of trees cut down in one month
    trees_cut_in_one_month = trees_cut_in_one_day * 30  # assuming there are 30 days in each month

    # Calculate the number of months it will take to cut down all the trees
    months_to_cut_all_trees = total_trees // trees_cut_in_one_month

    result = months_to_cut_all_trees
    return result

print(solution())