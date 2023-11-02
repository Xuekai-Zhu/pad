def solution():
    bowls_to_deliver = 638
    safe_bowls = bowls_to_deliver - 12 - 15

    # Calculate the total amount paid by the home goods store for delivered bowls
    delivered_payment = 3 * safe_bowls

    # Calculate the total amount paid by Travis for lost or broken bowls
    lost_payment = 4 * (12 + 15)

    # Calculate Travis's total payment
    total_payment = delivered_payment - lost_payment + 100
    result = total_payment
    return result

print(solution())