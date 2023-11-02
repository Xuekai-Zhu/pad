def solution():
    """Stephen placed an online order for groceries. His final bill came to $40.00. Because this was through a delivery vendor, they tacked on a 25% fee to his final total and charged him $3.00 in delivery fees. Stephen also added a $4.00 tip. After the extra fees, what was the final price of Stephen's groceries?"""
    final_bill = 40.00
    delivery_fee = 3.00
    tip = 4.00
    extra_fees = (final_bill * 0.25) + delivery_fee + tip
    total_cost = final_bill + extra_fees
    result = total_cost
    return result

print(solution())