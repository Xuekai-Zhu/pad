def solution():
    """A school canteen sells a sandwich at $2, a hamburger at $2, one stick of hotdog at $1, and a can of fruit juice at $2 each can. Selene buys three sandwiches and a can of fruit juice. Tanya buys two hamburgers and two cans of fruit juice. How much do Selene and Tanya spend together?"""
    sandwich_price = 2
    hamburger_price = 2
    hotdog_price = 1
    fruit_juice_price = 2
    selene_spend = 3 * sandwich_price + fruit_juice_price
    tanya_spend = 2 * hamburger_price + 2 * fruit_juice_price
    total_spend = selene_spend + tanya_spend
    result = total_spend
    return result

print(solution())