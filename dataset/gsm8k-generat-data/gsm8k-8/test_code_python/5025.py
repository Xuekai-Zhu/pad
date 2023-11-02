def solution():
    # Calculate the total cost of training for the first applicant
    training_cost = 3 * 1200

    # Calculate the total cost of hiring the first applicant
    first_applicant_cost = 42000 + training_cost

    # Calculate the total cost of hiring the second applicant
    second_applicant_cost = 45000 + (0.01 * 45000)

    # Calculate the total revenue from hiring the first applicant
    first_applicant_revenue = 93000 - first_applicant_cost

    # Calculate the total revenue from hiring the second applicant
    second_applicant_revenue = 92000 - second_applicant_cost

    # Calculate the difference in revenue between the two applicants
    revenue_difference = first_applicant_revenue - second_applicant_revenue
    result = revenue_difference
    return result

print(solution())