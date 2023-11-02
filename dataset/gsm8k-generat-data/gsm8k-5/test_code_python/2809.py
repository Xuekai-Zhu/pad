def solution():
    # Calculate the current property tax bill
    current_value = 400000
    tax_rate = 0.02
    current_tax = current_value * tax_rate

    # Calculate the new value of the house after the high-speed rail project
    increased_value = current_value * 1.25

    # Calculate the new property tax bill
    new_tax = increased_value * tax_rate

    # Calculate the maximum amount she can spend on improvements without going over the budget
    max_improvement_value = (current_value + increased_value) / 2 - (current_tax + new_tax) - 15000

    result = max_improvement_value
    return result

print(solution())