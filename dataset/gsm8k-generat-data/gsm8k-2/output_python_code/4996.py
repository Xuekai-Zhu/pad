def solution():
    """In 2004, there were 60 kids at a cookout. In 2005, half the number of kids came to the cookout as compared to 2004. In 2006, 2/3 as many kids came to the cookout as in 2005. How many kids came to the cookout in 2006?"""
    year_1_kids = 60
    year_2_kids = year_1_kids // 2
    year_3_kids = (2/3) * year_2_kids
    total_kids = year_1_kids + year_2_kids + year_3_kids
    result = total_kids
    return result

print(solution())