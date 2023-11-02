def solution():
    
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