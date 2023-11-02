def solution():
    novels_per_month = 4  # I read 4 novels per month
    pages_per_novel = 200  # Each novel has 200 pages
    months_per_year = 12  # There are 12 months in a year

    # Calculate the total number of pages I will read in a year
    total_pages = novels_per_month * pages_per_novel * months_per_year
    result = total_pages
    return result

print(solution())