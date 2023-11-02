def solution():
    """Vicente bought 5 kilograms of rice and 3 pounds of meat. Each kilogram of rice is $2 and a pound of meat is $5. How much did Vicente spend in total?"""
    # Define the prices per unit
    RICE_PRICE = 2
    MEAT_PRICE = 5

    # Define the quantities purchased
    rice_kgs = 5
    meat_lbs = 3

    # Calculate the total cost of the rice and meat respectively
    rice_cost = rice_kgs * RICE_PRICE
    meat_cost = meat_lbs * MEAT_PRICE

    # Calculate the total cost
    total_cost = rice_cost + meat_cost

    # Display the result
    result = total_cost
    return result

print(solution())