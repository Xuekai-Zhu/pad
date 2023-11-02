def solution():
    """Simon wanted to buy flowers that his mom could plant for Mother's Day. The garden center was offering 10% off all purchases. He bought 5 pansies at $2.50 each, one hydrangea that cost $12.50 and 5 petunias that cost $1.00 each. If he paid with a $50 bill, how much change would Simon receive back from his purchase?"""
    pansies = 5 * 2.5
    hydrangea = 12.5
    petunias = 5 * 1
    subtotal = pansies + hydrangea + petunias
    discount = 0.1 * subtotal
    total = subtotal - discount
    change = 50 - total
    result = change
    return result

print(solution())