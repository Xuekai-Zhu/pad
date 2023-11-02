def solution():
    """Jimmy is a pizza delivery man. Each pizza costs 12 dollars and the delivery charge is 2 extra dollars if the area is farther than 1 km from the pizzeria. Jimmy delivers 3 pizzas in the park, which is located 100 meters away from the pizzeria. Also, he delivers 2 pizzas in a building 2 km away from the pizzeria. How much money did Jimmy get paid for the pizzas?"""
    pizzas_in_park = 3
    pizzas_in_building = 2
    pizza_cost = 12
    delivery_charge = 2
    
    distance_park = 0.1
    distance_building = 2.0
    
    if distance_park > 1:
        total_cost_park = (pizzas_in_park * pizza_cost) + delivery_charge
    else:
        total_cost_park = pizzas_in_park * pizza_cost
        
    if distance_building > 1:
        total_cost_building = (pizzas_in_building * pizza_cost) + delivery_charge
    else:
        total_cost_building = pizzas_in_building * pizza_cost
        
    total_cost = total_cost_park + total_cost_building
    result = total_cost
    
    return result

print(solution())