def solution():
    """Maria has a pen and a pencil. She bought the pen for half the price of the pencil. The pencil cost her $8. How much did Maria pay for both the pen and the pencil?"""
    # Define the cost of the pencil
    PENCIL_PRICE = 8

    # Calculate the cost of the pen
    PEN_PRICE = PENCIL_PRICE / 2

    # Calculate the total cost of the pen and the pencil
    total_cost = PEN_PRICE + PENCIL_PRICE

    # Display the total cost
    result = total_cost
    return result

print(solution())