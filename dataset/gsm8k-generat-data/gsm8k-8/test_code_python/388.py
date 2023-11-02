def solution():
    # Calculate the total monthly income from subletting
    monthly_income = 3 * 400

    # Calculate the annual income from subletting
    annual_income = monthly_income * 12

    # Calculate the profit by subtracting the annual rental cost from the annual income
    profit = annual_income - (900 * 12)
    result = profit
    return result

print(solution())