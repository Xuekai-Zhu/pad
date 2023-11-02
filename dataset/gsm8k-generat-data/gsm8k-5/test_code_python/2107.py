def solution():
    monthly_salary = 5000  # Rhett is paid $5000 per month
    tax_rate = 0.10  # Rhett has to pay 10% tax
    net_salary = monthly_salary * (1 - tax_rate)  # Rhett's net monthly salary

    # Calculate the total cost of the two late rent payments
    late_rent = 2 * 1000  # Assume Rhett pays $1000 in rent per month
    total_cost = late_rent

    # Calculate Rhett's rent expense per month
    rent_expense = total_cost / (3/5 * net_salary)
    result = rent_expense
    return result

print(solution())