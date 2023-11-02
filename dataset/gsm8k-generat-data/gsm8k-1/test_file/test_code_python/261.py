def solution():
    """Mrs. Cruz is looking for a house that will not go beyond her $400 000 budget. She saw a property that has a selling price of $350 000. On top of that, the buyer has to pay a brokerage fee which is 5% of the selling price, and also the transfer fee that is 12% of the selling price. How much more is the total price of the house than Mrs. Cruz's budget?"""
    budget = 400000
    selling_price = 350000
    brokerage_fee = selling_price * 0.05
    transfer_fee = selling_price * 0.12
    total_cost = selling_price + brokerage_fee + transfer_fee
    difference = total_cost - budget
    result = difference
    return result

print(solution())