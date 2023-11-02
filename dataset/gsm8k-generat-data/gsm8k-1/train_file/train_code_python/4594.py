def solution():
    """If I read 4 novels with 200 pages each in a month, how many pages of novels will I read in a year?"""
    novels_per_month = 4
    pages_per_novel = 200
    months_per_year = 12
    total_pages = novels_per_month * pages_per_novel * months_per_year
    result = total_pages
    return result

print(solution())