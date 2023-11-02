def solution():
    """Jimmy is a pizza delivery man. Each pizza costs 12 dollars and the delivery charge is 2 extra dollars if the area is farther than 1 km from the pizzeria. Jimmy delivers 3 pizzas in the park, which is located 100 meters away from the pizzeria. Also, he delivers 2 pizzas in a building 2 km away from the pizzeria. How much money did Jimmy get paid for the pizzas?"""
    pizza_price = 12
    far_delivery_charge = 2
    park_distance = 100  # meters
    far_delivery_distance = 2000  # meters
    park_pizza_cost = (pizza_price * 3)
    far_pizza_cost = (pizza_price * 2) + far_delivery_charge
    total_cost = park_pizza_cost + far_pizza_cost
    result = total_cost
    return result

print(solution())