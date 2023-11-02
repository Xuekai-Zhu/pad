def solution():
    initial_salary = 1000000
    new_salary = 1500000
    initial_tax_rate = 0.2
    new_tax_rate = 0.3

    # Calculate the initial tax amount based on 20% tax rate
    initial_tax_amount = initial_salary * initial_tax_rate

    # Calculate the new tax amount based on 30% tax rate
    new_tax_amount = new_salary * new_tax_rate

    # Calculate the difference in tax amount
    tax_difference = new_tax_amount - initial_tax_amount
    result = tax_difference
    return result

print(solution())