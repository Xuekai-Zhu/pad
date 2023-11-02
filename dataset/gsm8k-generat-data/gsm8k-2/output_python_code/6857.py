def solution():
    """A luxury perfume costs $1200. The store owner decided to increase its price by 10% so that he could earn more profit. Few weeks had past but the perfume was still not sold. So, the owner decided to lower the price by 15%. By how much was the final price lower than the original price?"""
    original_price = 1200
    increased_price = original_price * 1.1
    decreased_price = increased_price * 0.85
    final_price_lowered = original_price - decreased_price
    result = final_price_lowered
    return result

print(solution())