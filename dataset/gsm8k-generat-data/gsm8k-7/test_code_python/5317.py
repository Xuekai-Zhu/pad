def solution():
    medical_expenses = 128
    salary = 160

    # Calculate half of the medical expenses
    half_medical_expenses = medical_expenses / 2

    # Calculate the total amount that the house help will receive after deducting the other half of the medical expenses from her salary
    total_salary = salary - half_medical_expenses

    # Calculate the total amount that each of the couple should pay for the house help's expenses
    total_expenses = (medical_expenses / 2) + (salary / 2)

    # Calculate the amount that the husband still needs to pay for the house help's expenses
    husband_payment = total_expenses / 2
    result = husband_payment - half_medical_expenses
    return result

print(solution())