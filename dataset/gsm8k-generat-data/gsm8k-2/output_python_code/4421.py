def solution():
    """A smartphone seller is offering a discount of 5% off for customers who buy at least 2 smartphones at once. Melinda, Zoe and Joel want to buy an iPhone X each. If an iPhone X costs $600, how much can they save by pooling their money together and buying three iPhones at once from this seller rather than buying individually?"""
    individual_price = 600
    total_price = 3 * individual_price
    discount = 0
    if total_price >= 1200:
        discount = 0.05 * total_price
    total_price_with_discount = total_price - discount
    individual_price_with_discount = total_price_with_discount / 3
    total_savings = 3 * (individual_price - individual_price_with_discount)
    result = total_savings
    return result

print(solution())