def solution():
    """Kyle has a newspaper-delivery route. Every Monday through Saturday, he delivers the daily paper for the 100 houses on his route. 
    On Sunday, 10 of his customers do not get the Sunday paper, but he delivers 30 papers to other houses that get the newspaper only on Sunday. 
    How many papers does Kyle deliver each week?"""
    
    # Define the number of papers delivered each day except Sunday
    daily_papers = 100

    # Define the number of customers who do not get Sunday paper
    sunday_non_customers = 10

    # Define the number of Sunday-only customers
    sunday_only_customers = 30

    # Calculate the total number of papers delivered each week
    total_papers = (daily_papers * 6) + (daily_papers - sunday_non_customers + sunday_only_customers)

    # Display the total number of papers delivered each week
    result = total_papers
    return result

print(solution())