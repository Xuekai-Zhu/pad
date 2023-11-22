def solution():
    
    notebook_price = 1.5
    pen_price = 0.25
    calculator_price = 12
    geometry_price = 10
    num_notebooks = 5
    num_pens = 2
    num_calculators = 1
    num_geometry_sets = 1
    total_price = (notebook_price * num_notebooks) + (pen_price * num_pens) + (calculator_price * num_calculators) + (geometry_price * num_geometry_sets)
    discount = total_price * 0.1
    total_price -= discount
    result = total_price
    return result

print(solution())