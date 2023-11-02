def solution():
    
    first_year_growth = 2
    second_year_growth = first_year_growth * 1.5
    third_year_growth = second_year_growth * 1.5
    fourth_year_growth = third_year_growth * 2
    fifth_year_growth = fourth_year_growth * 0.5
    total_growth = first_year_growth + second_year_growth + third_year_growth + fourth_year_growth + fifth_year_growth
    result = total_growth
    return result

print(solution())