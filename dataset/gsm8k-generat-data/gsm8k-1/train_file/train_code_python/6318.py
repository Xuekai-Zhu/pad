def solution():
    """Jean needs to buy 10 new pairs of pants. A store is running a sale for 20% off. If the pants normally retail for $45 each how much will she need to pay for all of them after paying a 10% tax?"""
    num_pants = 10
    retail_price = 45
    percent_off = 20
    sale_price = retail_price - (retail_price * (percent_off / 100))
    subtotal = num_pants * sale_price
    tax_percent = 10
    total_cost = subtotal + (subtotal * (tax_percent / 100))
    result = total_cost
    return result

print(solution())