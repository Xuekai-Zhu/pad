def solution():
    total_employees = 100  # assume 100 total employees for ease of calculation
    women_percent = 60
    men_percent = 100 - women_percent

    # Calculate the number of men in the company
    men_count = (men_percent / 100) * total_employees

    # Calculate the number of men without a college degree
    men_without_degree = 8

    # Calculate the number of men with a college degree
    men_with_degree = men_count - men_without_degree

    # Calculate the number of women in the company
    women_count = (women_percent / 100) * total_employees

    # Calculate the number of women with a college degree
    women_with_degree = (men_with_degree * 0.25) / 0.75

    result = women_count + women_with_degree
    return result

print(solution())