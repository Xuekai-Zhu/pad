def solution():
    # Calculate the total earnings of Kristy
    basic_pay = 7.5 * 160
    commission = 0.16 * 25000
    total_earnings = basic_pay + commission

    # Calculate the amount allocated for expenses and insurance
    expenses = 0.95 * total_earnings
    insurance = total_earnings - expenses

    result = insurance
    return result

print(solution())