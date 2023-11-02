def solution():
    novels_per_month = 4
    pages_per_novel = 200
    months_per_year = 12

    # Calculate the total number of pages of novels read in one month
    total_pages_per_month = novels_per_month * pages_per_novel

    # Calculate the total number of pages of novels read in a year
    total_pages_per_year = total_pages_per_month * months_per_year
    result = total_pages_per_year
    return result

print(solution())