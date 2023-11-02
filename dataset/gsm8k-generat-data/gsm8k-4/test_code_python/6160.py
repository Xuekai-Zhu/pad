def solution():
    """The cash price of a refrigerator was $8000. Samantha wanted to buy the refrigerator but pay in installments. If she paid a deposit of $3000 and paid 30 equal monthly installments of $300 each, calculate how much money she would have saved by paying cash."""
    # Define the cash price of the refrigerator
    cash_price = 8000

    # Define the amount paid as deposit
    deposit = 3000

    # Define the number of monthly installments
    num_installments = 30

    # Define the amount paid per installment
    installment_payment = 300

    # Calculate the total amount paid if bought with installments
    total_installment_payment = deposit + (num_installments * installment_payment)

    # Calculate the total amount saved by paying cash
    total_savings = cash_price - total_installment_payment

    result = total_savings
    return result

print(solution())