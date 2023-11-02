def solution():
    """A couple agreed to split their expenses equally, including the salary of their house help. While doing her job, the house help had an accident; thus, she underwent a medical procedure which cost her $128. The couple decided to pay half of the medical expenses and the other half will be deducted from her $160 salary. If the husband paid for the entire half of the hospital bill, how much does he still need to pay so that they split the expenses for the house help equally?"""
    medical_expenses = 128
    half_medical_expenses = medical_expenses/2
    salary = 160
    half_salary_deduction = salary - half_medical_expenses
    equal_expenses = (half_medical_expenses + half_salary_deduction)/2
    amount_to_be_paid = equal_expenses - half_medical_expenses
    result = amount_to_be_paid
    return result

print(solution())