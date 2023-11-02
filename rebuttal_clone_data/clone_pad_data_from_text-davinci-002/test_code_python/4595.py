def solution():
    novels_read_per_month = 4
    pages_per_novel = 200
    pages_read_per_month = novels_read_per_month * pages_per_novel
    pages_read_per_year = pages_read_per_month * 12
    result = pages_read_per_year
    return result

print(solution())