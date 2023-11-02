def solution():
    # Total trees cut down by James in first 2 days
    james_trees_day1 = 20
    james_trees_day2 = 20
    james_total_trees_days1_2 = james_trees_day1 + james_trees_day2

    # Trees cut down per day by James and his brothers in the next 3 days
    james_trees_day3 = 20 * 0.8
    brother_trees_day3 = james_trees_day3
    james_trees_day4 = 20 * 0.8
    brother_trees_day4 = james_trees_day4
    james_trees_day5 = 20 * 0.8
    brother_trees_day5 = james_trees_day5

    # Total trees cut down by James and his brothers in the next 3 days
    total_trees_james_days3_5 = james_trees_day3 + james_trees_day4 + james_trees_day5
    total_trees_brothers_days3_5 = brother_trees_day3 + brother_trees_day4 + brother_trees_day5
    total_trees_james_and_brothers_days3_5 = total_trees_james_days3_5 + total_trees_brothers_days3_5

    # Total trees cut down over 5 days
    total_trees_cut_down = james_total_trees_days1_2 + total_trees_james_and_brothers_days3_5
    result = total_trees_cut_down
    return result

print(solution())