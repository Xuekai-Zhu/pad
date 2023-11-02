def solution():
    """The cash price of a refrigerator was $8000. Samantha wanted to buy the refrigerator but pay in installments. If she paid a deposit of $3000 and paid 30 equal monthly installments of $300 each, calculate how much money she would have saved by paying cash."""
    # Define the cash price of the refrigerator
    CASH_PRICE = 8000

    # Calculate the total amount paid with installments
    total_paid = 3000 + (30 * 300)

    # Calculate the amount saved by paying cash
    amount_saved = CASH_PRICE - total_paid

    # Display the amount saved
    result = amount_saved
    return result

print(solution())