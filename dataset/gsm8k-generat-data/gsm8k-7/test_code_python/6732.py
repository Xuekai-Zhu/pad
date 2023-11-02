def solution():
    num_years_1 = 3
    income_1 = 30000
    percentage_1 = 0.3

    num_years_2 = 4
    income_2 = income_1 * 1.2
    percentage_2 = 0.3

    total_income = (num_years_1 * income_1) + (num_years_2 * income_2)

    total_owed = total_income * percentage_1

    total_owed += (num_years_2 * income_2 * percentage_2)

    amount_paid = 1200

    amount_owed = total_owed - amount_paid
    result = amount_owed
    return result

print(solution())