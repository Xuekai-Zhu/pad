def solution():
    """Leo collects stickers. Two years ago, he had 100 stickers in his collection. Last year, Leo collected 50 stickers. This year, he collected twice the number of stickers as the previous year. How many stickers does Leo have in his collection?"""
    two_years_ago = 100
    last_year = 50
    this_year = last_year * 2
    total_stickers = two_years_ago + last_year + this_year
    result = total_stickers
    return result

print(solution())