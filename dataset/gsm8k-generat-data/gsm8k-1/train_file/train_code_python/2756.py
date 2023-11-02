def solution():
    """Aryan owes Fernanda $1200, which is twice what Kyro owes Fernanda. Aryan decides to pay 60% of her debt to Fernanda, and Kyro pays Fernanda 80% of her dept. If Fernanda had $300 in her savings account and adds the money she's been paid by her debtors to the savings account, calculate the total amount of money in her savings account now."""
    kyro_debt = 1200 / 2
    aryan_debt = 1200
    kyro_paid = kyro_debt * 0.8
    aryan_paid = aryan_debt * 0.6
    total_paid = kyro_paid + aryan_paid
    total_savings = 300 + total_paid
    result = total_savings
    return result

print(solution())