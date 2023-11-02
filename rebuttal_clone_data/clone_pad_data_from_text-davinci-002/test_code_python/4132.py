def solution():
    first_year = 2
    second_year = first_year + (first_year * 0.5)
    third_year = second_year + (second_year * 0.5)
    fourth_year = third_year + (third_year)
    fifth_year = fourth_year + (fourth_year * 0.5)
    result = fifth_year
    
    return result

print(solution())