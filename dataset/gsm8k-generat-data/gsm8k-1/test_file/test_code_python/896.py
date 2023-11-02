def solution():
    """Denise and Daniel are reading the same book. Yesterday, Denise read 10 pages while Daniel read 13 pages. Today, Denise read 5 more than as many pages as what Daniel read yesterday, while Daniel was not able to read any pages today. How many more pages did Denise read more than Daniel?"""
    yesterday_daniel = 13
    today_daniel = 0
    yesterday_denise = 10
    today_denise = yesterday_daniel + 5
    total_daniel = yesterday_daniel + today_daniel
    total_denise = yesterday_denise + today_denise
    more_pages = total_denise - total_daniel
    result = more_pages
    return result

print(solution())