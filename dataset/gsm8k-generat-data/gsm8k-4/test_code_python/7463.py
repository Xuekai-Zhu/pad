def solution():
    """An office has 90 workers. 2/3rds of them are men and the rest are women. The company hires 10 new employees and 100% of them are women. What is the total percentage of women in the company now?"""
    # Define the total number of workers
    total_workers = 90

    # Calculate the number of men
    men = total_workers * (2/3)

    # Calculate the number of women
    women = total_workers - men

    # Hire 10 new employees, all women
    women += 10

    # Calculate the percentage of women in the company now
    women_percentage = (women / (men + women)) * 100

    # return the result
    result = women_percentage
    return result

print(solution())