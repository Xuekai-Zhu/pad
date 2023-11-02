def solution():
    annual_income = 65000
    annual_rent = 20000
    annual_groceries = 5000
    annual_gas = 8000
    minimum_savings = 42000

    # Calculate Logan's total expenses
    total_expense = annual_rent + annual_groceries + annual_gas

    # Calculate Logan's total income after expenses and minimum savings
    required_income = total_expense + minimum_savings
    additional_income_needed = required_income - annual_income
    result = additional_income_needed
    return result

print(solution())