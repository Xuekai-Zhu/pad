def solution():
    """Loisa wants to buy a tablet that costs $450 cash. Since she does not have enough money, the store offered her
    an installment plan for 12 months. She will pay $100 as a down payment and pay $40 for the first 4 months;
    then $35 for the next four months; then $30 for the last four months. How much will Loisa save if she will buy
    the tablet in cash instead of on installment?"""
    # Compute the total cost of the tablet with the installment plan
    total_cost_installment = 450 + (40 * 4) + (35 * 4) + (30 * 4) - 100

    # Compute the cost of the tablet if purchased in cash (no interest)
    total_cost_cash = 450

    # Compute the amount saved by purchasing in cash
    amount_saved = total_cost_installment - total_cost_cash

    # Return the result
    result = amount_saved
    return result

print(solution())