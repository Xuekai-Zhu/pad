def solution():
    # Calculate the cost per bagel when buying individually
    bagel_indiv_cost = 225  # $2.25 in cents
    bagel_indiv_savings = 0   # savings per bagel when buying individually is 0 since there is no discount

    # Calculate the cost per bagel when buying by the dozen
    bagel_dozen_cost = 2000/12  # $24 divided by 12 bagels
    bagel_dozen_savings = (bagel_indiv_cost - bagel_dozen_cost)/12  # divide the total savings by 12 to get savings per bagel

    result = bagel_dozen_savings
    return result

print(solution())