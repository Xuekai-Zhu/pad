def solution():
    """Piazzanos Pizzeria has a buy-1-get-1-free special on triple cheese pizzas, and a buy-2-get-1-free special on meat lovers pizzas. 
    If the standard price for a pizza is $5, how much does it cost, in dollars, to purchase 10 triple cheese and 9 meat lovers pizzas using the special pricing?"""
    
    triple_cheese_price = 5 / 2 # Buy-1-get-1-free
    meat_lovers_discount = 2 / 3 # Buy-2-get-1-free
    meat_lovers_price = meat_lovers_discount * 5
    
    total_triple_cheese = 10 # number of triple cheese pizzas
    total_meat_lovers = 9 # number of meat lovers pizzas
    
    cost_triple_cheese = total_triple_cheese * triple_cheese_price
    cost_meat_lovers = (total_meat_lovers // 2 * meat_lovers_price) + (total_meat_lovers % 2 * 5)
    total_cost = cost_triple_cheese + cost_meat_lovers
    
    result = total_cost
    return result

print(solution())