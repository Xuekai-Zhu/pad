def solution():
    # Define initial variables
    dashboard_balance = 4000
    first_client_payment = dashboard_balance / 2
    second_client_payment = 2/5 * first_client_payment + first_client_payment
    third_client_payment = 2 * (first_client_payment + second_client_payment)

    # Calculate total payment and add to dashboard balance
    total_payment = first_client_payment + second_client_payment + third_client_payment
    dashboard_balance += total_payment

    result = dashboard_balance
    return result

print(solution())