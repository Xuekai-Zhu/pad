def solution():
    
    initial_quarters = 50
    first_year_quarters = initial_quarters * 2
    second_year_quarters = first_year_quarters + (3 * 12)
    third_year_quarters = second_year_quarters + (int(12 / 3))
    lost_quarters = int(third_year_quarters / 4)
    remaining_quarters = third_year_quarters - lost_quarters
    result = remaining_quarters
    return result

print(solution())