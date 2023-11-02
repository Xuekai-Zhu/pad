def solution():
    # Calculate the total cost of the medical procedure
    total_medical_cost = 128 * 2  # the couple agreed to split the cost equally

    # Calculate the total cost to be split equally between the couple and the house help
    total_expense = total_medical_cost + 160  # half of the medical expense will be deducted from the house help's salary

    # Calculate the amount that the husband still needs to pay to equalize their expenses
    husband_payment = total_expense / 2 - 64  # the husband paid for the entire half of the medical bill, so he needs to pay half of the remaining $64
    result = husband_payment
    return result

print(solution())