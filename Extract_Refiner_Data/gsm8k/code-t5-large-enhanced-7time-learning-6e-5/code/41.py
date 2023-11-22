def solution():
    
    # Define the number of articles written on Monday and Tuesday
    monday_articles = 5
    tuesday_articles = monday_articles * (2/5) + monday_articles

    # Define the number of articles written on Wednesday
    wednesday_articles = tuesday_articles * 2

    # Define the average time spent writing each article
    research_time = 4
    tuesday_time = tuesday_articles * research_time
    wednesday_time = wednesday_articles * research_time

    # Calculate the total time spent writing articles in three days
    total_time = (monday_articles + tuesday_articles + wednesday_articles) * research_time

    # return the result
    result = total_time
    return result

print(solution())