def solution():
    
    hamburger_price = 5
    cola_price = 2
    discount = 4
    hamburgers = 2
    colas = 3
    total_price = (hamburgers * hamburger_price) + (colas * cola_price) - discount
    result = total_price
    return result

print(solution())