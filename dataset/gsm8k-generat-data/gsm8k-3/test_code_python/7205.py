def solution():
    """Marc bought 5 model cars that cost $20 each and 5 bottles of paint that cost $10 each. He also bought 5 paintbrushes that cost $2 each. How much did Marc spend in total?"""
    # Define the prices of each item
    CAR_PRICE = 20
    PAINT_PRICE = 10
    BRUSH_PRICE = 2

    # Define the quantities of each item purchased
    car_quantity = 5
    paint_quantity = 5
    brush_quantity = 5

    # Calculate the total cost of the model cars
    car_cost = car_quantity * CAR_PRICE

    # Calculate the total cost of the paint bottles
    paint_cost = paint_quantity * PAINT_PRICE

    # Calculate the total cost of the paintbrushes
    brush_cost = brush_quantity * BRUSH_PRICE

    # Calculate the total cost of all the items
    total_cost = car_cost + paint_cost + brush_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())