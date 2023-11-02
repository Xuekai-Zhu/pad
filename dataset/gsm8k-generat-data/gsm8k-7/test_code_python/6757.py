def solution():
    annual_salary_loss = 50000 * 30
    medical_bills = 200000
    punitive_damages = 3 * (medical_bills + annual_salary_loss)
    total_claim = annual_salary_loss + medical_bills + punitive_damages
    settlement_amount = 0.8 * total_claim
    result = settlement_amount
    return result

print(solution())