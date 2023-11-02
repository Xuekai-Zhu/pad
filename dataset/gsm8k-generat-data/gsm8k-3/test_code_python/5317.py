def solution():
    """A couple agreed to split their expenses equally, including the salary of their house help. While doing her job, the house help had an accident; thus, she underwent a medical procedure which cost her $128. The couple decided to pay half of the medical expenses and the other half will be deducted from her $160 salary. If the husband paid for the entire half of the hospital bill, how much does he still need to pay so that they split the expenses for the house help equally?"""
    # Calculate the total cost of the medical procedure
    total_medical_cost = 128

    # Calculate the amount each person should pay for the medical procedure
    each_person_cost = (total_medical_cost / 2) / 2

    # Calculate the amount the husband needs to pay
    husband_cost = each_person_cost - (160 / 2)

    # Display the amount the husband needs to pay
    result = husband_cost
    return result

print(solution())