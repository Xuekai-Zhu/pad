def solution():
    coffee_price = 4
    cake_price = 7
    ice_cream_price = 3
    
    # Mell's order
    mell_order = 2 * coffee_price + cake_price
    
    # Friends' order
    friends_order = (2 * coffee_price) + cake_price + (2 * ice_cream_price)
    
    # Total cost
    total_cost = mell_order + friends_order
    result = total_cost
    return result

print(solution())