def solution():
    appetizer = 8
    steak_price = 20
    wine_price = 3
    dessert = 6
    
    # Total cost before discount
    total_cost = appetizer + steak_price + (2 * wine_price) + dessert
    
    # Cost after discount
    discounted_cost = (steak_price / 2) + appetizer + (2 * wine_price) + dessert
    
    # Cost with tip
    total_with_tip = discounted_cost * 1.2
    
    result = total_with_tip
    return result

print(solution())