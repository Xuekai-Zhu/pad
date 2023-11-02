def solution():
    """Jimmy is a pizza delivery man. Each pizza costs 12 dollars and the delivery charge is 2 extra dollars if the area is farther than 1 km from the pizzeria. Jimmy delivers 3 pizzas in the park, which is located 100 meters away from the pizzeria. Also, he delivers 2 pizzas in a building 2 km away from the pizzeria. How much money did Jimmy get paid for the pizzas?"""
    # Define the cost per pizza and the delivery charge
    PIZZA_PRICE = 12
    DELIVERY_CHARGE = 2

    # Define the distance for the park and the building
    PARK_DISTANCE = 0.1
    BUILDING_DISTANCE = 2

    # Calculate the total pizza cost for the park delivery
    park_pizza_cost = 3 * PIZZA_PRICE

    # Check if the delivery charge applies for the park delivery
    if PARK_DISTANCE > 1:
        park_delivery_cost = DELIVERY_CHARGE
    else:
        park_delivery_cost = 0

    # Calculate the total pizza cost for the building delivery
    building_pizza_cost = 2 * PIZZA_PRICE

    # Check if the delivery charge applies for the building delivery
    if BUILDING_DISTANCE > 1:
        building_delivery_cost = DELIVERY_CHARGE
    else:
        building_delivery_cost = 0

    # Calculate the total cost for both deliveries
    total_cost = park_pizza_cost + park_delivery_cost + building_pizza_cost + building_delivery_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())