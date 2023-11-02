def solution():
    """At Sarah's job 60% of the employees are women and the rest are men. Of the men, 75% have a college degree and 8 do not. How many women work at Sarah's company?"""
    # Define the total number of employees
    total_employees = 100

    # Calculate the number of men
    men = total_employees - (total_employees * 0.6)

    # Calculate the number of men with a college degree
    men_college_degree = men * 0.75

    # Calculate the number of men without a college degree
    men_no_college_degree = 8

    # Calculate the number of women
    women = total_employees * 0.6

    # return the result
    result = women
    return result

print(solution())