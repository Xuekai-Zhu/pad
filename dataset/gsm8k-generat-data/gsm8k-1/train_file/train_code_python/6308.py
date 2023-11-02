def solution():
    """Maddox and Theo both bought 3 Polaroid Cameras, each sold at $20 per camera from Amazon, and decided to sell them on eBay. Maddox sold his cameras at $28 each, while Theo sold his cameras at $23 each. How much more profit did Maddox get from the sale of his cameras than Theo?"""
    cameras_bought = 3
    amazon_price = 20
    maddox_sale_price = 28
    theo_sale_price = 23
    
    maddox_profit = (maddox_sale_price - amazon_price) * cameras_bought
    theo_profit = (theo_sale_price - amazon_price) * cameras_bought
    
    profit_difference = maddox_profit - theo_profit
    result = profit_difference
    
    return result

print(solution())