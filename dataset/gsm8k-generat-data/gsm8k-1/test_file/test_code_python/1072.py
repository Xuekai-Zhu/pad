def solution():
    """Terry sells 6 milkshakes for $5.50 each, nine burger platters for $11 each, and 20 sodas for $1.50 each. How much money does he make in total?"""
    milkshake_price = 5.50
    burger_price = 11
    soda_price = 1.50
    num_milkshakes = 6
    num_burgers = 9
    num_sodas = 20
    total_sales = (milkshake_price * num_milkshakes) + (burger_price * num_burgers) + (soda_price * num_sodas)
    result = total_sales
    return result

print(solution())