def solution():
    """A luxury perfume costs $1200. The store owner decided to increase its price by 10% so that he could earn more profit. Few weeks had past but the perfume was still not sold. So, the owner decided to lower the price by 15%. By how much was the final price lower than the original price?"""
    original_price = 1200
    increase_percent = 10
    decrease_percent = 15
    
    increased_price = original_price + (original_price * (increase_percent / 100))
    decreased_price = increased_price - (increased_price * (decrease_percent / 100))
    price_difference = original_price - decreased_price
    
    result = price_difference
    return result

print(solution())