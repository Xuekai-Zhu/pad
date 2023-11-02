def solution():
    
    croissant_price = 4.5
    plain_croissant_price = 3.0
    focaccia_price = 4.0
    latte_price = 2.5
    num_almond_croissants = 1
    num_salami_cheese_croissants = 1
    num_plain_croissants = 1
    num_focaccia = 1
    num_lattes = 2
    total_cost = (num_almond_croissants + num_salami_cheese_croissants) * croissant_price + num_plain_croissants * plain_croissant_price + num_focaccia * focaccia_price + num_lattes * latte_price
    result = total_cost
    return result

print(solution())