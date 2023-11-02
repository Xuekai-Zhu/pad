def solution():
    """Tobias is a tractor salesman. His salary is based on the number of tractors he sells. 
    For every red tractor he sells, he gets paid 10% of the sales price for each tractor. 
    For every green tractor he sells, he gets paid 20% of the sales price for each tractor. 
    This week, he sold 2 red tractors and 3 green tractors. 
    The price of a single red tractor is $20,000. 
    This week, Tobias's salary was $7000. 
    What is the full price of a single green tractor, in dollars?"""
    
    red_price = 20000
    red_commission = red_price * 0.1
    green_commission = 7000 - (red_commission * 2)
    green_price = green_commission / (0.2 * 3)
    result = green_price
    
    return result

print(solution())