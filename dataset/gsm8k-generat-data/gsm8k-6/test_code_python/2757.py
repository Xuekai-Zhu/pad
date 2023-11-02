def solution():
    # Calculate the amount Kyro owes Fernanda
    kyro_debt = 1200 / 2

    # Calculate the amount Aryan pays Fernanda
    aryan_payment = 0.6 * 1200

    # Calculate the amount Kyro pays Fernanda
    kyro_payment = 0.8 * kyro_debt

    # Calculate the total amount in Fernanda's savings account after receiving payment
    total_savings = 300 + aryan_payment + kyro_payment
    result = total_savings
    return result

print(solution())