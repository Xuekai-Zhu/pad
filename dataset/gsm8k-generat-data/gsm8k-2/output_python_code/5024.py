def solution():
    """A professional company is hiring for a new position. They have two qualified applicants. The first applicant will accept a salary of $42000 and make the company $93000 in the first year,
    but needs 3 months of additional training that costs $1200 a month. The second applicant does not need training and will make the company $92000 in the first year,
    but is requesting a salary of $45000 and a hiring bonus of 1% of his salary. Less the amount it will cost to pay for each candidate,
    how many more dollars will one candidate make the company than the other in the first year?"""
    applicant1_salary = 42000
    applicant1_training_cost = 1200 * 3
    applicant1_revenue = 93000
    applicant1_total_cost = applicant1_salary + applicant1_training_cost

    applicant2_salary = 45000
    applicant2_hiring_bonus = 0.01 * applicant2_salary
    applicant2_revenue = 92000
    applicant2_total_cost = applicant2_salary + applicant2_hiring_bonus

    applicant1_profit = applicant1_revenue - applicant1_total_cost
    applicant2_profit = applicant2_revenue - applicant2_total_cost

    result = abs(applicant1_profit - applicant2_profit)
    return result

print(solution())