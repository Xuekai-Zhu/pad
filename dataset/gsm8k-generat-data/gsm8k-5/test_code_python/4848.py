def solution():
    # Calculate the percentage of men in the company
    men_percentage = 100 - 60  # 60% of employees are women

    # Calculate the number of men without a college degree
    men_no_degree = 8  # Given in the question

    # Calculate the total number of men in the company
    men_total = (100 - 60) / 100 * 1000  # Assume there are a total of 1000 employees, so 100% = 1000

    # Calculate the number of men with a college degree
    men_with_degree = men_total - men_no_degree
    men_degree_percentage = 75  # Given in the question
    men_degree_total = men_with_degree / (men_degree_percentage / 100)

    # Calculate the number of women in the company
    women_total = 1000 - men_total
    women_percentage = 60  # Given in the question
    women_with_degree = women_total - men_degree_total
    women_degrees_percentage = 100 - men_degree_percentage
    women_degrees_total = women_with_degree / (women_degrees_percentage / 100)
    result = women_total - women_degrees_total
    return result

print(solution())