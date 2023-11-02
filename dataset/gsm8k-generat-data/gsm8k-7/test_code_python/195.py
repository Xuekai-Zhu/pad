def solution():
    num_drink_boxes = 5
    drink_box_price = 6

    num_pizza_boxes = 10
    pizza_box_price = 14

    total_paid = 200

    # Calculate the total cost of all drinks
    total_drink_cost = num_drink_boxes * drink_box_price

    # Calculate the total cost of all pizzas
    total_pizza_cost = num_pizza_boxes * pizza_box_price

    # Calculate the total cost of all items
    total_cost = total_drink_cost + total_pizza_cost

    # Calculate the change
    change = total_paid - total_cost
    result = change
    return result

print(solution())