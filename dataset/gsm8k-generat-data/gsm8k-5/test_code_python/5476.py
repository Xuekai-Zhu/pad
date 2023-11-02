def solution():
    pizza_cost = 12  # Each pizza costs 12 dollars
    delivery_charge = 2  # Delivery charge is 2 extra dollars for distances farther than 1 km

    # Calculate the total amount earned for pizzas delivered in the park
    distance_park = 0.1  # Distance to the park is 100 meters = 0.1 km
    if distance_park <= 1:
        charge_park = 0
    else:
        charge_park = delivery_charge
    amount_park = (pizza_cost * 3) + (charge_park * 3)  # Jimmy delivers 3 pizzas in the park

    # Calculate the total amount earned for pizzas delivered in the building
    distance_building = 2  # Distance to the building is 2 km
    if distance_building <= 1:
        charge_building = 0
    else:
        charge_building = delivery_charge
    amount_building = (pizza_cost * 2) + (charge_building * 2)  # Jimmy delivers 2 pizzas in the building

    # Calculate the total amount earned for all pizzas delivered
    total_amount = amount_park + amount_building
    result = total_amount
    return result

print(solution())