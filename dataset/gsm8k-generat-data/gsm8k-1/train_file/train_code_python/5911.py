def solution():
    """A school canteen sells a sandwich at $2, a hamburger at $2, one stick of hotdog at $1, and a can of fruit juice at $2 each can. Selene buys three sandwiches and a can of fruit juice. Tanya buys two hamburgers and two cans of fruit juice. How much do Selene and Tanya spend together?"""
    sandwich_price = 2
    hamburger_price = 2
    hotdog_price = 1
    juice_price = 2
    
    # Selene's purchase
    selene_sandwiches = 3
    selene_juice = 1
    selene_total_cost = (selene_sandwiches * sandwich_price) + (selene_juice * juice_price)
    
    # Tanya's purchase
    tanya_hamburgers = 2
    tanya_juice = 2
    tanya_total_cost = (tanya_hamburgers * hamburger_price) + (tanya_juice * juice_price)
    
    # Total cost
    total_cost = selene_total_cost + tanya_total_cost
    result = total_cost
    return result

print(solution())