def solution():
    """Aryan owes Fernanda $1200, which is twice what Kyro owes Fernanda. Aryan decides to pay 60% of her debt to Fernanda, 
    and Kyro pays Fernanda 80% of her dept. If Fernanda had $300 in her savings account and adds the money she's been paid 
    by her debtors to the savings account, calculate the total amount of money in her savings account now."""
    # Calculate Kyro's debt to Fernanda
    kyro_debt = 1200 / 2

    # Calculate the amount Aryan pays
    aryan_payment = 1200 * 0.6

    # Calculate the amount Kyro pays
    kyro_payment = kyro_debt * 0.8

    # Calculate the total amount Fernanda has now
    total_savings = 300 + aryan_payment + kyro_payment

    # Display the total amount
    result = total_savings
    return result

print(solution())