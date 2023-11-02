def solution():
    """Yesterday Ryan got five books from the library. They were a total of 2100 pages. His brother got one book a day that was 200 pages each. They both finished them in a week. On average, how many more pages per day did Ryan read compared to his brother?"""
    ryan_total_pages = 2100
    ryan_avg_pages_per_day = ryan_total_pages / 7
    brother_total_pages = 7 * 200
    brother_avg_pages_per_day = brother_total_pages / 7
    pages_per_day_more = ryan_avg_pages_per_day - brother_avg_pages_per_day
    result = pages_per_day_more
    return result

print(solution())