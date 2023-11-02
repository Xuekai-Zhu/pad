def solution():
    
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