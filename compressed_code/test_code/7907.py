def solution():
    
    pieces_per_pizza = 8
    pieces_per_day = 3
    days = 72
    total_pizzas = (pieces_per_day * days) / pieces_per_pizza
    result = total_pizzas
    return result

print(solution())