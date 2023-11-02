def solution():
    """Simon wanted to buy flowers that his mom could plant for Mother's Day. The garden center was offering 10% off all purchases. He bought 5 pansies at $2.50 each, one hydrangea that cost $12.50 and 5 petunias that cost $1.00 each. If he paid with a $50 bill, how much change would Simon receive back from his purchase?"""
    pansies = 5
    price_pansies = 2.50
    hydrangea = 1
    price_hydrangea = 12.50
    petunias = 5
    price_petunias = 1.00
    bill_amount = 50.00
    total_amount = pansies * price_pansies + hydrangea * price_hydrangea + petunias * price_petunias
    discount_amount = total_amount * 0.10
    total_due = total_amount - discount_amount
    change_amount = bill_amount - total_due
    result = change_amount
    
    return result

print(solution())