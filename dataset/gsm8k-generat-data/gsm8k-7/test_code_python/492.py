def solution():
    num_judges = 40
    percent_under_30 = 0.10
    percent_30_to_50 = 0.60

    # Calculate the number of judges under 30 years old
    num_under_30 = num_judges * percent_under_30

    # Calculate the number of judges between 30 and 50 years old
    num_30_to_50 = num_judges * percent_30_to_50

    # Calculate the number of judges over 50 years old
    num_over_50 = num_judges - num_under_30 - num_30_to_50

    result = num_over_50
    return result

print(solution())