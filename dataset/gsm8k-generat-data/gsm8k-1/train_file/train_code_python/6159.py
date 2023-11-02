def solution():
    """The cash price of a refrigerator was $8000. Samantha wanted to buy the refrigerator but pay in installments. If she paid a deposit of $3000 and paid 30 equal monthly installments of $300 each, calculate how much money she would have saved by paying cash."""
    cash_price = 8000
    deposit = 3000
    total_paid = deposit + 30 * 300
    amount_saved = cash_price - total_paid
    result = amount_saved
    return result

print(solution())