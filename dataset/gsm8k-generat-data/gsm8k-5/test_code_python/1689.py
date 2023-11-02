def solution():
    current_dashboard = 4000  # Baylor currently has $4000 on his dashboard
    first_client_payment = current_dashboard / 2  # The first client pays Baylor half of his current dashboard
    second_client_payment = first_client_payment * (2/5) + first_client_payment  # The second client pays 2/5 more than the first client
    total_payment = first_client_payment + second_client_payment  # The total payment from the first two clients
    third_client_payment = total_payment * 2  # The third client pays twice the amount of the first two clients combined
    total_payment += third_client_payment  # Add the payment from the third client to the total payment

    final_dashboard = current_dashboard + total_payment  # Add the total payment to Baylor's current dashboard
    result = final_dashboard
    return result

print(solution())