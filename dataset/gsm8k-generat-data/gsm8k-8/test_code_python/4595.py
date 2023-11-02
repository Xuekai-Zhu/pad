def solution():
    # Define the number of novels read in a month and the number of pages per novel
    novels_per_month = 4
    pages_per_novel = 200

    # Calculate the total number of pages read in a month
    pages_per_month = novels_per_month * pages_per_novel

    # Calculate the total number of pages read in a year
    pages_per_year = pages_per_month * 12
    result = pages_per_year
    return result

print(solution())