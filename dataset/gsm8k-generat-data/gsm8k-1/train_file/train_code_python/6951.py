def solution():
    """Lauren wanted to make burgers and fries for dinner. She needed a few things from the grocery store and bought 
    the following: 2 pounds of hamburger meat that was on sale for $3.50 a pound. 1 pack of hamburger buns for $1.50. 
    A head of lettuce for $1.00 and a large 1.5-pound tomato that was priced at $2.00 per pound. She also needed a jar 
    of pickles that cost $2.50 and she had a $1.00 off coupon for that item. How much change would Lauren get back if 
    she paid with a $20 bill?"""
    hamburger_meat_price = 3.5
    hamburger_meat_weight = 2
    hamburger_buns_price = 1.5
    lettuce_price = 1.0
    tomato_price = 2.0
    tomato_weight = 1.5
    pickles_price = 2.5
    pickles_discount = 1.0
    total_cost = (hamburger_meat_price * hamburger_meat_weight) + hamburger_buns_price + lettuce_price + (tomato_price * tomato_weight) + (pickles_price - pickles_discount)
    change = 20 - total_cost
    result = change
    return result

print(solution())