def solution():
    """Regina wrote 9 novels last year. If this is 3 quarters of the number of novels she has written this year, how many novels has she written this year?"""
    novels_last_year = 9
    percent_written_this_year = 75
    novels_this_year = novels_last_year / (percent_written_this_year / 100)
    result = novels_this_year
    return result

print(solution())