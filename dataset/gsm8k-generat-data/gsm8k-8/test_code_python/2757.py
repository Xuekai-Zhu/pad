def solution():
    # Calculate the amount Kyro owes Fernanda
    kyro_owes = 1200 / 2

    # Calculate the amount Aryan pays back
    aryan_paid = 0.6 * 1200

    # Calculate the amount Kyro pays back
    kyro_paid = 0.8 * kyro_owes

    # Calculate the total amount of money Fernanda has now
    total_savings = 300 + aryan_paid + kyro_paid
    result = total_savings
    return result

print(solution())