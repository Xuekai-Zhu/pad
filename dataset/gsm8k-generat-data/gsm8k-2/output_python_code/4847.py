def solution():
    """At Sarah's job 60% of the employees are women and the rest are men. Of the men, 75% have a college degree and 8 do not. How many women work at Sarah's company?"""
    total_employees = 100  # assume 100 employees for ease of calculation
    women_percent = 60
    men_percent = 100 - women_percent
    men_no_degree = 8
    men_with_degree = ((men_percent / 100) * total_employees) - men_no_degree
    total_women = (women_percent / 100) * total_employees
    women_no_degree = total_employees - men_with_degree - men_no_degree - total_women
    result = total_women - women_no_degree  # subtract the uneducated women to get the final answer
    return result

print(solution())