def solution():
    initial_amount = 3000
    monthly_amount = 276
    number_of_months = 4 * 12
    total_amount = initial_amount + (monthly_amount * number_of_months) + 7000
    result = total_amount
    return result

print(solution())