def solution():
    # Define the cost of each pizza and the delivery charge
    pizza_cost = 12
    delivery_charge = 2

    # Calculate the total cost of the pizzas delivered in the park
    park_distance = 0.1
    park_delivery_charge = 0 if park_distance <= 1 else delivery_charge
    park_total_cost = (pizza_cost * 3) + park_delivery_charge

    # Calculate the total cost of the pizzas delivered in the building
    building_distance = 2
    building_delivery_charge = 0 if building_distance <= 1 else delivery_charge
    building_total_cost = (pizza_cost * 2) + building_delivery_charge

    # Calculate the total amount of money Jimmy was paid
    total_paid = park_total_cost + building_total_cost
    result = total_paid
    return result

print(solution())