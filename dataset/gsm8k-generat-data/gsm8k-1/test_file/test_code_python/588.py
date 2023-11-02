def solution():
    """Marilyn wants to buy a pair of boots online. On Amazon.com, the boots cost $16 and shipping costs $4. On eBay, those same pair of shoes are only $13, but shipping costs twice as much as it does on Amazon. How much more expensive do the boots work out to be on eBay?"""
    amazon_price = 16
    amazon_shipping = 4
    ebay_price = 13
    ebay_shipping = 2 * amazon_shipping
    amazon_total_cost = amazon_price + amazon_shipping
    ebay_total_cost = ebay_price + ebay_shipping
    price_difference = ebay_total_cost - amazon_total_cost
    result = price_difference
    return result

print(solution())