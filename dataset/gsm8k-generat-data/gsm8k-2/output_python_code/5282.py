def solution():
    """
    Cody goes to the store and buys $40 worth of stuff. The taxes were 5%. After taxes, he got an $8 discount. Cody and his friend split the final price equally. How much did Cody pay?
    """
    subtotal = 40
    tax_rate = 0.05
    discount = 8

    # Calculate total with tax and discount
    total = (subtotal * (1 + tax_rate)) - discount

    # Divide total by 2 to split with friend
    cody_paid = total / 2

    result = cody_paid
    return result

print(solution())