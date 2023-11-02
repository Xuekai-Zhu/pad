def solution():
    """Meredith is a freelance blogger who writes about health topics and submits to clients each day as her permanent job. A blog article takes an average of 4 hours to research and write about. Last week, she wrote 5 articles on Monday and  2/5 times more articles on Tuesday than on Monday. On Wednesday, she wrote twice the number of articles she wrote on Tuesday. Calculate the total number of hours she spent writing articles in the three days."""
    articles_monday = 5
    articles_tuesday = articles_monday * (2/5) + articles_monday
    articles_wednesday = articles_tuesday * 2
    total_articles = articles_monday + articles_tuesday + articles_wednesday
    hours_per_article = 4
    total_hours = total_articles * hours_per_article
    result = total_hours
    return result

print(solution())