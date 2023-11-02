def solution():
    # Calculate the total number of months Gunther will make payments for
    total_months = 5 * 12

    # Calculate the total amount Gunther will pay for the tractor
    total_payment = 150 * total_months

    # Calculate the amount Gunther financed by dividing the total payment by the number of months
    financed_amount = total_payment / total_months
    result = financed_amount
    return result

print(solution())