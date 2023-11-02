def solution():
    """Kyle has a newspaper-delivery route. Every Monday through Saturday, he delivers the daily paper for the 100 houses on his route. On Sunday, 10 of his customers do not get the Sunday paper, but he delivers 30 papers to other houses that get the newspaper only on Sunday. How many papers does Kyle deliver each week?"""
    daily_papers = 100 * 6
    sunday_papers = (100 - 10) + 30
    total_papers = daily_papers + sunday_papers
    result = total_papers
    return result

print(solution())