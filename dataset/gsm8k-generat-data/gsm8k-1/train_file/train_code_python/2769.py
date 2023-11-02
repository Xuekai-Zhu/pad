def solution():
    """Robert and Teddy are planning to buy snacks for their friends.
    Robert orders five boxes of pizza at $10 each box and ten cans of soft drinks at $2 each.
    Teddy buys six hamburgers at $3 each and an additional ten cans of soft drinks.
    How much do they spend in all?"""
    
    robert_pizza_boxes = 5
    robert_pizza_box_cost = 10
    robert_soft_drinks = 10
    robert_soft_drink_cost = 2
    
    teddy_hamburgers = 6
    teddy_hamburger_cost = 3
    teddy_soft_drinks = 10
    teddy_soft_drink_cost = 2
    
    total_cost = (robert_pizza_boxes * robert_pizza_box_cost) + (robert_soft_drinks * robert_soft_drink_cost) + (teddy_hamburgers * teddy_hamburger_cost) + (teddy_soft_drinks * teddy_soft_drink_cost)
    
    result = total_cost
    return result

print(solution())