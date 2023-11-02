def solution():
    tuition_cost = 30000  # The total cost of Sabina's first year of college
    saved_money = 10000  # The amount Sabina has already saved

    # Calculate the remaining tuition cost after Sabina's savings
    remaining_tuition = tuition_cost - saved_money

    # Calculate the amount covered by the grant
    grant_amount = remaining_tuition * 0.4

    # Calculate the amount Sabina needs to apply for in a loan
    loan_amount = remaining_tuition - grant_amount
    result = loan_amount
    return result

print(solution())