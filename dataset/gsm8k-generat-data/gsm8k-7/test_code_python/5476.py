def solution():
    pizza_cost = 12
    far_delivery_charge = 2
    park_deliveries = 3
    far_deliveries = 2

    # Calculate the cost of delivering pizzas in the park
    park_delivery_cost = (pizza_cost * park_deliveries) + (far_delivery_charge * 0)

    # Calculate the cost of delivering pizzas far away
    far_delivery_cost = (pizza_cost * far_deliveries) + (far_delivery_charge * 2)

    # Calculate the total amount of money Jimmy earned
    total_earnings = park_delivery_cost + far_delivery_cost
    result = total_earnings
    return result

print(solution())