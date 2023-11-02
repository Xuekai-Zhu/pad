def solution():
    adidas_cost = 600  # Mimi spent $600 on Adidas sneakers
    skechers_cost = 5 * adidas_cost  # Mimi spent 1/5 of Skechers cost on Adidas
    nike_cost = 3 * adidas_cost  # Mimi spent three times as much on Nike as on Adidas
    total_cost = adidas_cost + skechers_cost + nike_cost  # Total cost of all sneakers

    # Calculate the amount spent on clothes
    clothes_cost = 8000 - total_cost
    result = clothes_cost
    return result

print(solution())