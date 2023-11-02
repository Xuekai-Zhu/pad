def solution():
    """Vicente bought 5 kilograms of rice and 3 pounds of meat. Each kilogram of rice is $2 and a pound of meat is $5. How much did Vicente spend in total?"""
    # Define the prices and amounts purchased
    RICE_PRICE = 2
    MEAT_PRICE = 5
    RICE_AMOUNT = 5
    MEAT_AMOUNT = 3

    # Calculate the total cost
    total_cost = (RICE_AMOUNT * RICE_PRICE) + (MEAT_AMOUNT * MEAT_PRICE)

    # Return the total cost
    result = total_cost
    return result

print(solution())