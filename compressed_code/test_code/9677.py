def solution():
    
    total_cost = 610
    known_prices = [49, 81]
    num_unknown_prices = 5
    unknown_price = (total_cost - sum(known_prices)) / num_unknown_prices
    result = unknown_price
    return result

print(solution())