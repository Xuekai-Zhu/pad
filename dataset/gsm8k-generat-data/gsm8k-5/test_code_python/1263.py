def solution():
    starting_quarters = 50  # Phil started with 50 state quarters
    doubled_quarters = starting_quarters * 2  # Phil doubled his collection the following year
    collected_quarters_year_3 = 3 * 12  # Phil collected 3 quarters each month in the third year
    collected_quarters_year_4 = 1 * (12 // 3)  # Phil collected 1 quarter every 3 months in the fourth year
    total_quarters = starting_quarters + doubled_quarters + collected_quarters_year_3 + collected_quarters_year_4
    lost_quarters = total_quarters // 4  # Phil lost a quarter of his collection
    remaining_quarters = total_quarters - lost_quarters
    result = remaining_quarters
    return result

print(solution())