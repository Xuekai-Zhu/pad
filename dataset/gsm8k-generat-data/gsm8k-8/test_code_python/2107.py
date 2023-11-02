def solution():
    # Calculate Rhett's monthly salary after taxes
    salary_after_tax = 5000 - (5000 * 0.1)

    # Calculate the total cost of Rhett's two late rent payments
    total_rent_cost = salary_after_tax * (2/5)

    # Calculate Rhett's monthly rent expense
    monthly_rent_expense = total_rent_cost / 2
    result = monthly_rent_expense
    return result

print(solution())