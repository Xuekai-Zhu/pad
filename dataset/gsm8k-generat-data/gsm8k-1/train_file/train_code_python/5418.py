def solution():
    """In 2004, there were some kids at a cookout. In 2005, half the number of kids came to the cookout as compared to 2004. In 2006, 2/3 as many kids came to the cookout as in 2005. If there were 20 kids at the cookout in 2006, how many kids came to the cookout in 2004?"""
    kids_2006 = 20
    kids_2005 = kids_2006 / (2/3)
    kids_2004 = 2 * kids_2005
    result = kids_2004
    return result

print(solution())