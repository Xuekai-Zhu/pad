def solution():
    starting_quarters = 50
    collected_quarters_year_1 = starting_quarters * 2
    collected_quarters_year_2 = 3 * 12
    collected_quarters_year_3 = 1 * (12/3)
    lost_quarters_year_4 = starting_quarters // 4

    total_quarters = starting_quarters + collected_quarters_year_1 + collected_quarters_year_2 + collected_quarters_year_3
    remaining_quarters = total_quarters - lost_quarters_year_4
    result = remaining_quarters
    return result

print(solution())