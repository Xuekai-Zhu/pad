def solution():
    """A couple agreed to split their expenses equally, including the salary of their house help. While doing her job, the house help had an accident; thus, she underwent a medical procedure which cost her $128. The couple decided to pay half of the medical expenses and the other half will be deducted from her $160 salary. If the husband paid for the entire half of the hospital bill, how much does he still need to pay so that they split the expenses for the house help equally?"""
    # Define the total cost of the medical procedure
    medical_cost = 128

    # Calculate the amount the couple pays for the medical bill
    couple_share = medical_cost / 2

    # Calculate the house help's salary after deducting the remaining medical bill
    remaining_salary = 160 - (medical_cost / 2)

    # Calculate the amount the husband still needs to pay to split the expenses equally
    equal_share = (couple_share + remaining_salary) / 2
    husband_share = equal_share - couple_share

    # return the result
    result = husband_share
    return result

print(solution())