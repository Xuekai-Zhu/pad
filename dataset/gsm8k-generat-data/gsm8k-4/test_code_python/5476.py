def solution():
    """Jimmy is a pizza delivery man. Each pizza costs 12 dollars and the delivery charge is 2 extra dollars if the area is farther than 1 km from the pizzeria. Jimmy delivers 3 pizzas in the park, which is located 100 meters away from the pizzeria. Also, he delivers 2 pizzas in a building 2 km away from the pizzeria. How much money did Jimmy get paid for the pizzas?"""
    # Define the pizza cost and delivery charge
    pizza_cost = 12
    delivery_charge = 2

    # Calculate the total amount earned for the pizzas delivered in the park
    park_distance = 0.1 # km
    if park_distance > 1:
        park_charge = delivery_charge
    else:
        park_charge = 0
    park_earnings = (pizza_cost * 3) + park_charge

    # Calculate the total amount earned for the pizzas delivered in the building
    building_distance = 2 # km
    if building_distance > 1:
        building_charge = delivery_charge
    else:
        building_charge = 0
    building_earnings = (pizza_cost * 2) + building_charge

    # Calculate the total amount earned by Jimmy for the pizzas
    total_earnings = park_earnings + building_earnings

    # return the result
    result = total_earnings
    return result

print(solution())