def solution():
    aryan_debt = 1200  # Aryan owes Fernanda $1200
    kyro_debt = aryan_debt / 2  # Kyro owes half of what Aryan owes
    aryan_payment = 0.6 * aryan_debt  # Aryan pays 60% of her debt
    kyro_payment = 0.8 * kyro_debt  # Kyro pays 80% of her debt

    # Calculate the total amount of money Fernanda has in her savings account
    total_savings = 300 + aryan_payment + kyro_payment
    result = total_savings
    return result

print(solution())