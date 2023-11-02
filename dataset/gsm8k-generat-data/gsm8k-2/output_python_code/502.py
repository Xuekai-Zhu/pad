def solution():
    """Yasna has two books. One book is 180 pages long, and the other book is 100 pages long. If Yasna wants to finish both of the books in two weeks, how many pages will Yasna need to read every day, if she reads an equal number of pages each day?"""
    total_pages = 180 + 100
    total_days = 14
    pages_per_day = total_pages / (total_days * 2) # since Yasna wants to finish both books in 2 weeks, she has to read an equal number of pages each day for 14 days
    result = pages_per_day
    return result

print(solution())