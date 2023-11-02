def solution():
    num_cars = 5
    car_price = 20

    num_paints = 5
    paint_price = 10

    num_brushes = 5
    brush_price = 2

    # Calculate the total cost of all model cars
    total_cars_cost = num_cars * car_price

    # Calculate the total cost of all bottles of paint
    total_paints_cost = num_paints * paint_price

    # Calculate the total cost of all paintbrushes
    total_brushes_cost = num_brushes * brush_price

    # Calculate the total cost of all items
    total_cost = total_cars_cost + total_paints_cost + total_brushes_cost
    result = total_cost
    return result

print(solution())