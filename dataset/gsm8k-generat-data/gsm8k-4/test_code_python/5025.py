def solution():
    """A professional company is hiring for a new position. They have two qualified applicants. The first applicant will accept a salary of $42000 and make the company $93000 in the first year, but needs 3 months of additional training that costs $1200 a month. The second applicant does not need training and will make the company $92000 in the first year, but is requesting a salary of $45000 and a hiring bonus of 1% of his salary. Less the amount it will cost to pay for each candidate, how many more dollars will one candidate make the company than the other in the first year?"""
    # Calculate the total cost of hiring the first applicant
    training_cost = 3 * 1200
    total_cost_first = 42000 + training_cost

    # Calculate the total cost of hiring the second applicant
    bonus = 0.01 * 45000
    total_cost_second = 45000 + bonus

    # Calculate the profits from each applicant
    profit_first = 93000 - total_cost_first
    profit_second = 92000 - total_cost_second

    # Calculate the difference in profits
    profit_difference = abs(profit_first - profit_second)

    # Determine which applicant generates more profit and by how much
    if profit_first > profit_second:
        result = profit_difference
    else:
        result = -profit_difference

    return result

print(solution())