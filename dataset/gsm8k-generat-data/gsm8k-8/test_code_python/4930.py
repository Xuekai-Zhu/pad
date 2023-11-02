def solution():
    # Calculate James' total trees cut in the first 2 days
    james_daily_trees = 20
    james_total_trees = james_daily_trees * 2

    # Calculate how many less trees James' brothers cut per day
    james_brothers_reduction = 0.20
    james_brothers_daily_trees = james_daily_trees - (james_brothers_reduction * james_daily_trees)

    # Calculate the total trees cut by James and his brothers
    total_days = 5
    total_trees_cut = james_total_trees + (james_brothers_daily_trees * total_days)

    result = total_trees_cut
    return result

print(solution())