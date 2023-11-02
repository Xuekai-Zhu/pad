def solution():
    
    total_tuition = 30000
    savings = 10000
    remaining_tuition = total_tuition - savings
    grant_percent = 40
    grant_amount = remaining_tuition * (grant_percent / 100)
    loan_amount = remaining_tuition - grant_amount
    result = loan_amount
    return result

print(solution())