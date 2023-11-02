def solution():
    """Jimmy and Irene go shopping for clothes on a Tuesday, where senior citizens get a 10% discount on their purchases. Jimmy picks out 3 shorts from the $15 rack. Irene grabs 5 shirts from the $17 rack. How much money do they give to the cashier?"""
    jimmy_shorts = 3
    jimmy_shorts_price = 15
    irene_shirts = 5
    irene_shirts_price = 17
    subtotal = jimmy_shorts * jimmy_shorts_price + irene_shirts * irene_shirts_price
    discount = 0.1 * subtotal
    total = subtotal - discount
    result = total
    return result

print(solution())