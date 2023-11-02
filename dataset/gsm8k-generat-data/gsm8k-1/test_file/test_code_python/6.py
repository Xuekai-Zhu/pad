def solution():
    """A new program had 60 downloads in the first month. The number of downloads in the second month was three times as many as the downloads in the first month, but then reduced by 30% in the third month. How many downloads did the program have total over the three months?"""
    
    first_month_downloads = 60
    second_month_downloads = 3 * first_month_downloads
    third_month_downloads = second_month_downloads - (0.3 * second_month_downloads)
    total_downloads = first_month_downloads + second_month_downloads + third_month_downloads
    result = total_downloads
    return result

print(solution())