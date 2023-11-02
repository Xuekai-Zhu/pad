def solution():
    # Calculate the total cost and revenue of making and selling bracelets
    cost = 3.00
    selling_price = 0.25
    total_bracelets = 52
    given_away = 8
    remaining_bracelets = total_bracelets - given_away
    revenue = remaining_bracelets * selling_price
    
    # Calculate the profit from selling the remaining bracelets
    profit = revenue - cost
    result = profit
    return result

print(solution())