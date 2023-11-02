def solution():
    
    total_tuition = 30000
    saved_amount = 10000
    remaining_tuition = total_tuition - saved_amount
    grant_amount = 0.4 * remaining_tuition
    loan_amount = remaining_tuition - grant_amount
    result = loan_amount
    return result

print(solution())