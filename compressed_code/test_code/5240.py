def solution():
    
    lyle_budget = 2.5
    sandwich_price = 0.3
    juice_price = 0.2
    total_price = sandwich_price + juice_price
    friends_count = int((lyle_budget - total_price) / total_price)

    result = friends_count
    return result

print(solution())