def solution():
    
    laptop_cost = 1000
    down_payment = laptop_cost * 0.2 + 20
    balance = laptop_cost - down_payment
    monthly_installment = 65
    remaining_months = 4
    for i in range(remaining_months):
        balance -= monthly_installment
    result = balance
    return result

print(solution())