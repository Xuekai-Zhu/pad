def solution():
    # Define the total cost and Sabina's savings
    total_cost = 30000
    savings = 10000

    # Calculate the remaining cost after accounting for savings
    remaining_cost = total_cost - savings

    # Calculate the amount covered by the grant
    grant_amount = remaining_cost * 0.4

    # Calculate the amount Sabina needs to apply for as a loan
    loan_amount = remaining_cost - grant_amount
    result = loan_amount
    return result

print(solution())