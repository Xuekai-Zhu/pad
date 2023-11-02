def solution():
    """A couple agreed to split their expenses equally, including the salary of their house help. While doing her job, the house help had an accident; thus, she underwent a medical procedure which cost her $128. The couple decided to pay half of the medical expenses and the other half will be deducted from her $160 salary. If the husband paid for the entire half of the hospital bill, how much does he still need to pay so that they split the expenses for the house help equally?"""
    medical_expenses = 128
    husband_paid = medical_expenses / 2
    remaining_expenses = medical_expenses - husband_paid
    house_help_salary = 160 - remaining_expenses
    equal_split = (medical_expenses + house_help_salary) / 2
    husband_to_pay = equal_split - husband_paid
    result = husband_to_pay
    return result

print(solution())