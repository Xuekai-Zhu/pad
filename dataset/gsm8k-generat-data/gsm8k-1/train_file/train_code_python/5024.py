def solution():
    """A professional company is hiring for a new position. They have two qualified applicants. The first applicant will accept a salary of $42000 and make the company $93000 in the first year, but needs 3 months of additional training that costs $1200 a month. The second applicant does not need training and will make the company $92000 in the first year, but is requesting a salary of $45000 and a hiring bonus of 1% of his salary. Less the amount it will cost to pay for each candidate, how many more dollars will one candidate make the company than the other in the first year?"""
    
    # Calculate the cost of the training for the first applicant
    training_cost = 3 * 1200
    
    # Calculate the total cost of the first applicant
    total_cost_applicant_1 = 42000 + training_cost
    
    # Calculate the profit from hiring the first applicant
    profit_applicant_1 = 93000 - total_cost_applicant_1
    
    # Calculate the total cost of the second applicant (including hiring bonus)
    total_cost_applicant_2 = 45000 + (0.01 * 45000)
    
    # Calculate the profit from hiring the second applicant
    profit_applicant_2 = 92000 - total_cost_applicant_2
    
    # Calculate the difference in profit between the two applicants
    difference = profit_applicant_2 - profit_applicant_1
    
    return difference

print(solution())