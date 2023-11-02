def solution():
    """Marc bought 5 model cars that cost $20 each and 5 bottles of paint that cost $10 each. He also bought 5 paintbrushes that cost $2 each. How much did Marc spend in total?"""
    # Define the prices and quantities of the items purchased
    model_car_price = 20
    model_car_qty = 5
    paint_price = 10
    paint_qty = 5
    brush_price = 2
    brush_qty = 5

    # Calculate the total cost of the model cars
    model_car_cost = model_car_price * model_car_qty

    # Calculate the total cost of the paint
    paint_cost = paint_price * paint_qty

    # Calculate the total cost of the paintbrushes
    brush_cost = brush_price * brush_qty

    # Calculate the total cost of the purchase
    total_cost = model_car_cost + paint_cost + brush_cost

    # return the result
    result = total_cost
    return result

print(solution())