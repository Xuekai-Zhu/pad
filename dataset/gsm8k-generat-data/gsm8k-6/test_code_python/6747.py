def solution():
    # Calculate the total gas expense for one day of commuting
    gas_expense_per_day = 21/30 * 2.5  # gas cost per mile * miles per day

    # Calculate the total gas expense for one person in a month
    gas_expense_per_person_per_month = gas_expense_per_day * 5 * 4  # commuting 5 days a week, 4 weeks a month

    # Calculate the amount each person should pay
    amount_per_person = gas_expense_per_person_per_month / 5  # split equally among 5 people
    result = amount_per_person
    return result

print(solution())