def solution():
    # Trees cut down by James in the first 2 days
    trees_james_day1 = 20
    trees_james_day2 = 20
    trees_james_first_2_days = trees_james_day1 + trees_james_day2

    # Trees cut down by James and his brothers in the next 3 days
    trees_james_per_day = 20
    trees_james_brothers_per_day = 0.8 * trees_james_per_day  # 20% fewer trees per day
    trees_james_day3 = trees_james_brothers_per_day
    trees_james_day4 = trees_james_brothers_per_day
    trees_james_day5 = trees_james_brothers_per_day
    trees_james_and_brothers_next_3_days = trees_james_day3 + trees_james_day4 + trees_james_day5

    # Total trees cut down
    total_trees_cut_down = trees_james_first_2_days + trees_james_and_brothers_next_3_days
    result = total_trees_cut_down
    return result

print(solution())