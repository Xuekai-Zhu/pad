def solution():
    # Define the cost of each item
    model_car_cost = 20
    paint_cost = 10
    paintbrush_cost = 2

    # Calculate the total cost of each item
    total_model_car_cost = 5 * model_car_cost
    total_paint_cost = 5 * paint_cost
    total_paintbrush_cost = 5 * paintbrush_cost

    # Calculate the total cost of all items
    total_cost = total_model_car_cost + total_paint_cost + total_paintbrush_cost
    result = total_cost
    return result

print(solution())