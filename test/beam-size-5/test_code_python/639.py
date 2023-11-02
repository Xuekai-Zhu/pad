def solution():
    
    political_articles_per_day = 20
    business_news_articles_per_day = 10
    days_in_month = 28
    total_political_articles = political_articles_per_day * days_in_month
    total_business_news_articles = business_news_articles_per_day * days_in_month
    total_articles = total_political_articles + total_business_news_articles
    result = total_articles
    return result

print(solution())