def solution():
    income = 65000  # Logan makes $65,000 a year
    expenses = 20000 + 5000 + 8000  # Logan spends $20,000 on rent, $5000 on groceries, and $8000 on gas
    minimum_savings = 42000  # Logan wants to have at least $42,000 left

    # Calculate how much more money Logan must make each year
    additional_income_needed = expenses + minimum_savings - income
    result = additional_income_needed
    return result

print(solution())