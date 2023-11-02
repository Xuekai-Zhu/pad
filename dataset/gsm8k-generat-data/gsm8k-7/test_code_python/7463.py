def solution():
    num_workers = 90
    men_ratio = 2/3
    women_ratio = 1 - men_ratio

    # Calculate the number of men and women in the company
    num_men = num_workers * men_ratio
    num_women = num_workers * women_ratio

    # Calculate the percentage of women in the company
    original_women_percentage = num_women / num_workers * 100

    # After hiring 10 more women, calculate the new total number of women and workers in the company
    new_num_women = num_women + 10
    new_num_workers = num_workers + 10

    # Calculate the new percentage of women in the company
    new_women_percentage = new_num_women / new_num_workers * 100
    result = new_women_percentage
    return result

print(solution())