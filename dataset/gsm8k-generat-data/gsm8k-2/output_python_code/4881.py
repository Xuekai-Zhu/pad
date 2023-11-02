def solution():
    """5/8 of shoppers at All Goods Available store prefer to avoid the check-out line on weekends and instead go through the express lane. If the number of shoppers in the store is 480, calculate the number of shoppers who pay at the check-out lane."""
    total_shoppers = 480
    express_shoppers = (5/8) * total_shoppers
    checkout_shoppers = total_shoppers - express_shoppers
    result = checkout_shoppers
    return result

print(solution())