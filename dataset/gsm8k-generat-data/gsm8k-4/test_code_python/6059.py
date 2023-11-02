def solution():
    """Kyle has a newspaper-delivery route. Every Monday through Saturday, he delivers the daily paper for the 100 houses on his route. On Sunday, 10 of his customers do not get the Sunday paper, but he delivers 30 papers to other houses that get the newspaper only on Sunday. How many papers does Kyle deliver each week?"""
    # Define the number of houses on Kyle's route
    houses = 100

    # Calculate the number of papers delivered from Monday to Saturday
    papers_weekdays = houses * 6

    # Calculate the number of papers delivered on Sunday
    papers_sunday = houses - 10 + 30

    # Calculate the total number of papers delivered
    papers_total = papers_weekdays + papers_sunday

    # return the result
    result = papers_total
    return result

print(solution())