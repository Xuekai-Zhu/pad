def solution():
    monthly_rent = 300
    monthly_rent_raise = 350
    months = 5 * 12
    total_amount_paid = monthly_rent * (months - 36) + monthly_rent_raise * 36
    result = total_amount_paid
    return result

print(solution())