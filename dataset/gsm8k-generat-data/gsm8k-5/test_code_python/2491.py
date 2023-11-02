def solution():
    # Calculate the income from selling fudge
    income_fudge = 20 * 2.5  # 20 pounds of fudge sold for $2.50 per pound

    # Calculate the income from selling chocolate truffles
    income_truffles = 5 * 12 * 1.5  # 5 dozen (60) chocolate truffles sold for $1.50 each

    # Calculate the income from selling chocolate-covered pretzels
    income_pretzels = 3 * 12 * 2  # 3 dozen (36) chocolate-covered pretzels sold for $2.00 each

    # Calculate the total income
    total_income = income_fudge + income_truffles + income_pretzels
    result = total_income
    return result

print(solution())