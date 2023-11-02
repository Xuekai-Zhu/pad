def solution():
     total_debt = 50
     debt_two_months_ago = 12
     debt_last_month = 15
     debt_still_owing = total_debt - (debt_two_months_ago + debt_last_month)
     result = debt_still_owing
     return result

print(solution())