def solution():
    tuition_cost = 30000
    savings = 10000
    grant_percent = 0.4

    # Calculate the amount of tuition that is not covered by Sabina's savings
    remaining_tuition = tuition_cost - savings

    # Calculate the amount of the remaining tuition that will be covered by the grant
    grant_amount = remaining_tuition * grant_percent

    # Calculate the total amount of tuition that Sabina will need to cover with a loan
    loan_amount = remaining_tuition - grant_amount
    result = loan_amount
    return result

print(solution())