def solution():
    initial_debt = 40
    paid_back = initial_debt / 2 
    additional_debt = 10

    # Calculate the total amount paid back so far
    total_paid_back = paid_back + additional_debt

    # Calculate the remaining debt that Tessa owes 
    remaining_debt = initial_debt - total_paid_back
    result = remaining_debt
    return result

print(solution())