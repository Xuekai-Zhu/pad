def solution():
    aryan_debt = 1200
    kyro_debt = aryan_debt / 2

    aryan_paid = 0.6 * aryan_debt
    kyro_paid = 0.8 * kyro_debt

    total_paid = aryan_paid + kyro_paid
    savings_account = 300 + total_paid

    result = savings_account
    return result

print(solution())