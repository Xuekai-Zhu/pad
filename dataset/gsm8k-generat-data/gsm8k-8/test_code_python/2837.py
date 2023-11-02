def solution():
    # Define the number of chocolate and strawberry cakes ordered and their respective prices
    num_chocolate = 3
    price_chocolate = 12
    num_strawberry = 6
    price_strawberry = 22

    # Calculate the total cost of the chocolate and strawberry cakes
    cost_chocolate = num_chocolate * price_chocolate
    cost_strawberry = num_strawberry * price_strawberry

    # Calculate the total cost of the order
    total_cost = cost_chocolate + cost_strawberry
    result = total_cost
    return result

print(solution())