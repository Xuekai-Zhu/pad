def solution():
    check_amount = 50  # Yasmin deposited a $50 check
    fraction_of_balance = 1/4  # The check is worth a quarter of her new balance

    # Calculate Yasmin's balance before depositing the check
    balance_before_check = (check_amount / fraction_of_balance) - check_amount
    result = balance_before_check
    return result

print(solution())