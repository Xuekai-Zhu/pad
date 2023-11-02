def solution():
    """A papaya tree will grow 2 feet in the first year. In the second year, it will grow 50% more than the first year. In the third year, the tree will grow 50% more than in the second year. In the fourth year, it will grow twice as much as the third year. In the fifth year, it will grow half as much as the fourth year. When the tree is 5 years old, how tall is the tree?"""
    year1_growth = 2
    year2_growth = year1_growth * 1.5
    year3_growth = year2_growth * 1.5
    year4_growth = year3_growth * 2
    year5_growth = year4_growth * 0.5

    total_height = year1_growth + year2_growth + year3_growth + year4_growth + year5_growth
    result = total_height

    return result

print(solution())