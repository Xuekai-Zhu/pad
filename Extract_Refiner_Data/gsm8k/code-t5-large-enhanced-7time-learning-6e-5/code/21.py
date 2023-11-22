def solution():
    
    # Define the prices of the items
    CHICKEN_MEAL_PRICE = 12
    MILK_PRICE = 3
    APPLE_PRICE = 1.5
    PIZZA_PRICE = 8.5

    # Define the quantities of each item ordered
    chicken_meal_qty = 1
    milk_qty = 5
    apple_qty = 4

    # Calculate the total cost of the items ordered
    total_cost = (chicken_meal_qty * CHICKEN_MEAL_PRICE) + (milk_qty * MILK_PRICE) + (apple_qty * APPLE_PRICE)

    # Calculate the cost of the pizza boxes
    pizza_cost = 50 - total_cost

    # Calculate the number of boxes of pizza ordered
    pizza_qty = pizza_cost / PIZZA_PRICE

    # Display the number of boxes of pizza ordered
    result =

print(solution())