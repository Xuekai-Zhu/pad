def solution():
    
    year1_growth = 2
    year2_growth = year1_growth * 1.5
    year3_growth = year2_growth * 1.5
    year4_growth = year3_growth * 2
    year5_growth = year4_growth * 0.5

    total_height = year1_growth + year2_growth + year3_growth + year4_growth + year5_growth
    result = total_height

    return result

print(solution())