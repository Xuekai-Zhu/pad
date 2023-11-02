def solution():
    """If I read 4 novels with 200 pages each in a month, how many pages of novels will I read in a year?"""
    # Define the number of novels read per month and the number of pages per novel
    novels_per_month = 4
    pages_per_novel = 200

    # Calculate the number of pages read per month
    pages_per_month = novels_per_month * pages_per_novel

    # Calculate the number of pages read per year
    pages_per_year = pages_per_month * 12

    # return the result
    result = pages_per_year
    return result

print(solution())