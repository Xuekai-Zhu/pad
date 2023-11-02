def solution():
    """Jean needs to buy 10 new pairs of pants. A store is running a sale for 20% off. If the pants normally retail for $45 each how much will she need to pay for all of them after paying a 10% tax?"""
    num_pants = 10
    pants_price = 45
    discount = 0.2
    sale_price = pants_price - (pants_price * discount)
    total_price = num_pants * sale_price
    tax_rate = 0.1
    total_price_with_tax = total_price + (total_price * tax_rate)
    result = total_price_with_tax
    return result

print(solution())