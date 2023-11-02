def solution():
    """Ali is a baker. Leila ordered 3 chocolate cakes for $12 each and 6 strawberry cakes for $22 each. How much should Leila pay Ali?"""
    # Define the prices and quantities of chocolate and strawberry cakes
    CHOCOLATE_PRICE = 12
    STRAWBERRY_PRICE = 22
    CHOCOLATE_QUANTITY = 3
    STRAWBERRY_QUANTITY = 6

    # Calculate the total cost of the chocolate cakes
    chocolate_cost = CHOCOLATE_PRICE * CHOCOLATE_QUANTITY

    # Calculate the total cost of the strawberry cakes
    strawberry_cost = STRAWBERRY_PRICE * STRAWBERRY_QUANTITY

    # Calculate the total cost of the order
    total_cost = chocolate_cost + strawberry_cost

    # return the result
    result = total_cost
    return result

print(solution())