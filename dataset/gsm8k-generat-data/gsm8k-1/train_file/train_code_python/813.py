def solution():
    """Every Sunday, Sean picks up 1 almond croissant and 1 salami and cheese croissant that are $4.50 each. He also grabs a plain croissant for $3.00 and a loaf of focaccia for $4.00. On his way home he stops and picks up 2 lattes for $2.50 each. How much did he spend?"""
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