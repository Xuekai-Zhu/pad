def solution():
    """Lauren wanted to make burgers and fries for dinner.  She needed a few things from the grocery store and bought the following:  2 pounds of hamburger meat that was on sale for $3.50 a pound.  1 pack of hamburger buns for $1.50.  A head of lettuce for $1.00 and a large 1.5-pound tomato that was priced at $2.00 per pound.  She also needed a jar of pickles that cost $2.50 and she had a $1.00 off coupon for that item.  How much change would Lauren get back if she paid with a $20 bill?"""
    
    # Define the prices of the items
    hamburger_price = 3.50
    bun_price = 1.50
    lettuce_price = 1.00
    tomato_price = 2.00
    pickle_price = 2.50

    # Define the quantities of the items
    hamburger_quantity = 2
    bun_quantity = 1
    lettuce_quantity = 1
    tomato_quantity = 1.5
    pickle_quantity = 1

    # Calculate the total cost of the items
    hamburger_cost = hamburger_price * hamburger_quantity
    bun_cost = bun_price * bun_quantity
    lettuce_cost = lettuce_price * lettuce_quantity
    tomato_cost = tomato_price * tomato_quantity
    pickle_cost = (pickle_price - 1) * pickle_quantity # taking into account the $1 off coupon

    total_cost = hamburger_cost + bun_cost + lettuce_cost + tomato_cost + pickle_cost

    # Calculate the change from a $20 bill
    change = 20 - total_cost

    # Return the change
    result = change
    return result

print(solution())