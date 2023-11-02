def solution():
    
    croissant_price = 4.5
    plain_croissant_price = 3.0
    focaccia_price = 4.0
    latte_price = 2.5
    num_croissants = 2
    num_lattes = 2
    total_cost = (croissant_price * num_croissants) + plain_croissant_price + focaccia_price + (latte_price * num_lattes)
    result = total_cost
    return result

print(solution())