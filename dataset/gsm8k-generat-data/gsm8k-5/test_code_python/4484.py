def solution():
    paycheck = 5000  # Diego's monthly paycheck
    expenses = 4600  # Diego's monthly expenses
    savings_per_month = paycheck - expenses  # Diego's monthly savings
    savings_per_year = savings_per_month * 12  # Diego's annual savings

    result = savings_per_year
    return result

print(solution())