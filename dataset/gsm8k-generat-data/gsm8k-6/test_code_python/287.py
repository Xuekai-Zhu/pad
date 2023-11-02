def solution():
    # Calculate the amount of the tuition fee that Bran needs to pay after the scholarship
    tuition_fee_after_scholarship = 0.7 * 90  # 30% of the tuition fee is covered by the scholarship

    # Calculate the total amount of money Bran earns from his part-time job
    total_earnings = 15 * 3

    # Calculate the amount Bran still needs to pay
    amount_to_pay = tuition_fee_after_scholarship - total_earnings

    result = amount_to_pay
    return result

print(solution())