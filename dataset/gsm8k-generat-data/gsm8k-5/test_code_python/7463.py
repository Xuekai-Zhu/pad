def solution():
    total_workers = 90  # The office has 90 workers
    men_percent = 2/3  # 2/3rds of the workers are men
    women_percent = 1 - men_percent  # The rest of the workers are women

    # Calculate the number of men and women in the company currently
    men_num = total_workers * men_percent
    women_num = total_workers * women_percent

    # Calculate the percentage of women in the company before the new hires
    women_percent_before = (women_num / total_workers) * 100

    # Add the new hires to the company
    total_workers += 10
    women_num += 10

    # Calculate the percentage of women in the company after the new hires
    women_percent_after = (women_num / total_workers) * 100

    # Calculate the total percentage of women in the company
    total_percent = (women_num / total_workers) * 100

    result = total_percent
    return result

print(solution())