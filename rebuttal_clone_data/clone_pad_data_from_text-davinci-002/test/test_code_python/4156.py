def solution():
    num_quarters = 76
    num_dimes = 85
    num_nickels = 20
    num_pennies = 150
    total_cents = num_quarters * 25 + num_dimes * 10 + num_nickels * 5 + num_pennies
    total_dollars = total_cents / 100
    fee = total_dollars * 0.10
    result = total_dollars - fee
    return result

print(solution())