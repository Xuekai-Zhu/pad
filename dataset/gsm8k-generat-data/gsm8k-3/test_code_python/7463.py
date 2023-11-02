def solution():
    """An office has 90 workers. 2/3rds of them are men and the rest are women. The company hires 10 new employees and 100% of them are women. What is the total percentage of women in the company now?"""
    # Calculate the number of men and women before hiring
    total_workers = 90
    men = total_workers * (2/3)
    women_before_hiring = total_workers - men

    # Calculate the number of women after hiring
    women_after_hiring = women_before_hiring + 10

    # Calculate the total number of workers after hiring
    total_workers_after_hiring = total_workers + 10

    # Calculate the percentage of women in the company after hiring
    percentage_women = (women_after_hiring / total_workers_after_hiring) * 100

    # Display the percentage of women in the company after hiring
    result = percentage_women
    return result

print(solution())