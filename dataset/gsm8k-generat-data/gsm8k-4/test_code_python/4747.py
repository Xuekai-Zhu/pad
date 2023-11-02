def solution():
    """Dr. Banks had 330 toothbrushes to give away to his patients. He gave away 53 toothbrushes in January. He gave away 67 toothbrushes in February. In March he gave away 46 toothbrushes. In April and May, he gave away the remaining toothbrushes, half each month. How many more toothbrushes did Dr. Banks give out in the busiest month versus the slowest month?"""
    # Calculate the total number of toothbrushes given away in the first three months
    total_given_away = 53 + 67 + 46

    # Calculate the number of toothbrushes left
    remaining_toothbrushes = 330 - total_given_away

    # Calculate the number of toothbrushes given away in April and May
    given_away_april = remaining_toothbrushes / 2
    given_away_may = remaining_toothbrushes / 2

    # Calculate the busiest and slowest months
    busiest_month = max(53, 67, 46, given_away_april, given_away_may)
    slowest_month = min(53, 67, 46, given_away_april, given_away_may)

    # Calculate the difference between the busiest and slowest months
    difference = busiest_month - slowest_month

    # return the result
    result = difference
    return result

print(solution())