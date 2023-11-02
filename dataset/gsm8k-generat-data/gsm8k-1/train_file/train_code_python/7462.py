def solution():
    """An office has 90 workers. 2/3rds of them are men and the rest are women. The company hires 10 new employees and 100% of them are women. What is the total percentage of women in the company now?"""
    total_workers = 90
    men = total_workers * (2/3)
    women = total_workers - men
    new_women = 10
    total_women = women + new_women
    total_workers = total_workers + 10
    percentage_women = (total_women / total_workers) * 100
    result = percentage_women
    return result

print(solution())