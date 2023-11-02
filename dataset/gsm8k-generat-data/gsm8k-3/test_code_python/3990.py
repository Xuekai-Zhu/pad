def solution():
    """A charity is delivering chicken and rice dinners to a shelter for the hungry. They have a hundred plates to deliver. The rice cost ten cents a plate and the chicken cost forty cents a plate. How many dollars did the charity spend on the food for the dinners?"""
    # Define the cost of rice and chicken per plate
    RICE_PRICE = 0.1
    CHICKEN_PRICE = 0.4

    # Define the number of plates to deliver
    plates = 100

    # Calculate the total cost of rice
    rice_cost = RICE_PRICE * plates

    # Calculate the total cost of chicken
    chicken_cost = CHICKEN_PRICE * plates

    # Calculate the total cost of the dinners
    total_cost = rice_cost + chicken_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())