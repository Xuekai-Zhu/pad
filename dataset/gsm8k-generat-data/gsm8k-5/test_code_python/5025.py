def solution():
    # Calculate the total cost for the first applicant
    cost_first_applicant = 42000 + (3 * 1200)

    # Calculate the total revenue for the first applicant
    revenue_first_applicant = 93000

    # Calculate the total cost for the second applicant
    cost_second_applicant = 45000 + (0.01 * 45000)

    # Calculate the total revenue for the second applicant
    revenue_second_applicant = 92000

    # Calculate the net profit for the first applicant
    profit_first_applicant = revenue_first_applicant - cost_first_applicant

    # Calculate the net profit for the second applicant
    profit_second_applicant = revenue_second_applicant - cost_second_applicant

    # Calculate the difference in net profit between the two applicants
    difference = profit_first_applicant - profit_second_applicant
    result = difference
    return result

print(solution())