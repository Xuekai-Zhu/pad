def solution():
    """Wilson goes to a fast-food restaurant. He buys 2 hamburgers for $5 each and 3 bottles of cola for $2 each. Wilson uses his $4 discount coupon. How much money does he pay in total?"""
    hamburgers = 2
    hamburger_price = 5
    colas = 3
    cola_price = 2
    discount = 4
    total_price = (hamburgers * hamburger_price) + (colas * cola_price) - discount
    result = total_price
    return result

print(solution())