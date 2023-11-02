def solution():
    total_cost = 30000
    saved_money = 10000
    grant_percent = 40
    grant_amount = (total_cost - saved_money) * (grant_percent / 100)
    loan_amount = total_cost - saved_money - grant_amount
    result = loan_amount
    return result

print(solution())