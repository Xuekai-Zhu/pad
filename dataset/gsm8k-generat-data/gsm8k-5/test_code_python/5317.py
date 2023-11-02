def solution():
    # Calculate the total cost of the medical procedure
    total_medical_cost = 2 * 128  # The couple agreed to split the cost equally, so the total cost is twice the original cost

    # Calculate the amount to be deducted from the house help's salary
    deducted_amount = 128 / 2  # Half of the medical expense will be deducted from her $160 salary

    # Calculate the total expense the couple needs to split equally, excluding the deducted amount
    total_expense = (total_medical_cost - deducted_amount) / 2

    # Calculate the amount the husband still needs to pay to split the expenses equally
    husband_share = total_expense - deducted_amount
    result = husband_share
    return result

print(solution())