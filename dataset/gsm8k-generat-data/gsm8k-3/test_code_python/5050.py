def solution():
    """Loisa wants to buy a tablet that costs $450 cash. Since she does not have enough money, the store offered her an installment plan for 12 months. She will pay $100 as a down payment and pay $40 for the first 4 months; then $35 for the next four months; then $30 for the last four months. How much will Loisa save if she will buy the tablet in cash instead of on installment?"""
    # Define the cash price of the tablet
    CASH_PRICE = 450

    # Define the total amount paid under the installment plan
    installment_price = 100 + (40 * 4) + (35 * 4) + (30 * 4)

    # Calculate the savings by buying in cash
    savings = installment_price - CASH_PRICE

    # Display the savings
    result = savings
    return result

print(solution())