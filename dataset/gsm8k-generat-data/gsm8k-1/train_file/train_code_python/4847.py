def solution():
    """At Sarah's job 60% of the employees are women and the rest are men. Of the men, 75% have a college degree and 8 do not. How many women work at Sarah's company?"""
    total_employees = 100  # Assume total number of employees is 100 for simplicity
    women_percent = 60
    men_percent = 100 - women_percent
    men_without_college = 8
    men_with_college = men_percent * (75 / 100) * total_employees
    total_men = men_without_college + men_with_college
    total_women = women_percent * total_employees / 100
    women_at_company = total_women
    
    return women_at_company

print(solution())