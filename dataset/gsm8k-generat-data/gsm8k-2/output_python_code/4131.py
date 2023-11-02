def solution():
    """A papaya tree will grow 2 feet in the first year. In the second year, it will grow 50% more than the first year. 
    In the third year, the tree will grow 50% more than in the second year. In the fourth year, it will grow twice as much 
    as the third year. In the fifth year, it will grow half as much as the fourth year. When the tree is 5 years old, 
    how tall is the tree?"""
    first_year_growth = 2
    second_year_growth = first_year_growth * 1.5
    third_year_growth = second_year_growth * 1.5
    fourth_year_growth = third_year_growth * 2
    fifth_year_growth = fourth_year_growth * 0.5
    total_growth = first_year_growth + second_year_growth + third_year_growth + fourth_year_growth + fifth_year_growth
    result = total_growth
    return result

print(solution())