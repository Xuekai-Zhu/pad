def solution():
    # Define the starting amount
    starting_amount = 2000

    # Subtract the payment to the supplier
    amount_after_supplier = starting_amount - 600

    # Add the payment from the debtor
    amount_after_debtor = amount_after_supplier + 800

    # Subtract the cost of equipment maintenance
    amount_remaining = amount_after_debtor - 1200

    result = amount_remaining
    return result

print(solution())