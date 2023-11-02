def solution():
    """Ali is a baker. Leila ordered 3 chocolate cakes for $12 each and 6 strawberry cakes for $22 each.  How much should Leila pay Ali?"""
    # Define the cost of each type of cake
    CHOCOLATE_CAKE_PRICE = 12
    STRAWBERRY_CAKE_PRICE = 22

    # Define the number of each type of cake
    chocolate_cakes = 3
    strawberry_cakes = 6

    # Calculate the cost of the chocolate cakes
    chocolate_cost = chocolate_cakes * CHOCOLATE_CAKE_PRICE

    # Calculate the cost of the strawberry cakes
    strawberry_cost = strawberry_cakes * STRAWBERRY_CAKE_PRICE

    # Calculate the total cost of the order
    total_cost = chocolate_cost + strawberry_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())