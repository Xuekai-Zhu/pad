def solution():
    # Calculate the total amount of damages Jerry is asking for
    salary_damages = 50000 * 30
    medical_damages = 200000
    punitive_damages = 3 * (salary_damages + medical_damages)
    total_damages = salary_damages + medical_damages + punitive_damages

    # Calculate the amount of money Jerry will get if he gets 80% of what he's asking for
    settlement_amount = 0.8 * total_damages
    result = settlement_amount
    return result

print(solution())