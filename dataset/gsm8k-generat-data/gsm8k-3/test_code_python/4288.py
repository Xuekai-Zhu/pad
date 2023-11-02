def solution():
    """Wilson goes to a fast-food restaurant. He buys 2 hamburgers for $5 each and 3 bottles of cola for $2 each. Wilson uses his $4 discount coupon. How much money does he pay in total?"""
    # Define the prices of the hamburgers and bottles of cola
    HAMBURGER_PRICE = 5
    COLA_PRICE = 2

    # Define the number of hamburgers and bottles of cola purchased
    hamburgers = 2
    cola_bottles = 3

    # Calculate the total cost of the hamburgers
    hamburger_cost = hamburgers * HAMBURGER_PRICE

    # Calculate the total cost of the bottles of cola
    cola_cost = cola_bottles * COLA_PRICE

    # Calculate the subtotal before discount
    subtotal = hamburger_cost + cola_cost

    # Apply the discount coupon
    subtotal -= 4

    # Display the total cost
    result = subtotal
    return result

print(solution())