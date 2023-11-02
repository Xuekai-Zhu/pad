def solution():
    """Yasna has two books. One book is 180 pages long, and the other book is 100 pages long. If Yasna wants to finish both of the books in two weeks, how many pages will Yasna need to read every day, if she reads an equal number of pages each day?"""
    total_pages = 180 + 100
    days_to_finish = 14
    pages_per_day = total_pages / days_to_finish
    result = pages_per_day
    return result

print(solution())