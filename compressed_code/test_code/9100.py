def solution():
    
    percent_spent = 35
    amount_spent = 14
    remaining_percent = 100 - percent_spent
    remaining_amount = (amount_spent / percent_spent) * remaining_percent
    result = remaining_amount
    return result

print(solution())