def solution():
    
    articles_monday = 5
    articles_tuesday = articles_monday * (2/5)
    articles_wednesday = articles_tuesday * 2
    total_articles = articles_monday + articles_tuesday + articles_wednesday
    total_time = total_articles * 4
    result = total_time
    return result

print(solution())