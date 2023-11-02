def solution():
    
    total_shoppers = 480
    express_shoppers = (5/8) * total_shoppers
    checkout_shoppers = total_shoppers - express_shoppers
    result = checkout_shoppers
    return result

print(solution())