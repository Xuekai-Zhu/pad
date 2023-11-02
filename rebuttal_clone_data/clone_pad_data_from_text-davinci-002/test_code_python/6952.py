def solution():
    hamburger_meat = 2
    sale_price_per_pound_meat = 3.50
    cost_of_hamburger_meat = hamburger_meat * sale_price_per_pound_meat
    hamburger_buns = 1
    cost_of_hamburger_buns = 1.50
    lettuce = 1
    cost_of_lettuce = 1.00
    tomato = 1.5
    price_per_pound_tomato = 2.00
    cost_of_tomato = tomato* price_per_pound_tomato
    pickles = 1
    cost_of_pickles = 2.50
    total_cost = cost_of_hamburger_meat + cost_of_hamburger_buns + cost_of_lettuce + cost_of_tomato + cost_of_pickles
    amount_paid = 20.00
    coupon_amount = 1.00
    total_amount_paid = amount_paid - coupon_amount
    change = total_amount_paid - total_cost
    result = change
    
    return

print(solution())