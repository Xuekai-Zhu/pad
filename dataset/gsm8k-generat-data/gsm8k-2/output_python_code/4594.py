def solution():
    """If I read 4 novels with 200 pages each in a month, how many pages of novels will I read in a year?"""
    pages_per_novel = 200
    novels_per_month = 4
    months_per_year = 12
    total_pages_per_year = pages_per_novel * novels_per_month * months_per_year
    result = total_pages_per_year
    return result

print(solution())