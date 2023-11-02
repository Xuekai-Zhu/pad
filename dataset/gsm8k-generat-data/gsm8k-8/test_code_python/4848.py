def solution():
    # Calculate the percentage of men at the company
    men_percentage = 100 - 60

    # Calculate the total number of employees (assuming there are no non-binary individuals)
    total_employees = 100

    # Calculate the number of men at the company
    men_count = int((men_percentage/100) * total_employees)

    # Calculate the number of men without a college degree
    men_no_degree = 8

    # Calculate the number of men with a college degree
    men_with_degree = int(((75/100) * men_count) - men_no_degree)

    # Calculate the number of women at the company
    women_count = total_employees - men_count

    # Calculate the number of women with a college degree
    women_with_degree = int((60/100) * women_count)

    result = women_count
    return result

print(solution())