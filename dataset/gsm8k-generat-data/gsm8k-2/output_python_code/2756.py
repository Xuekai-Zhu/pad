def solution():
    """Aryan owes Fernanda $1200, which is twice what Kyro owes Fernanda. Aryan decides to pay 60% of her debt to Fernanda, and Kyro pays Fernanda 80% of her dept. If Fernanda had $300 in her savings account and adds the money she's been paid by her debtors to the savings account, calculate the total amount of money in her savings account now."""
    aryan_debt = 1200
    kyro_debt = aryan_debt / 2
    aryan_payment = aryan_debt * 0.6
    kyro_payment = kyro_debt * 0.8
    total_money = aryan_payment + kyro_payment + 300
    result = total_money
    return result

print(solution())