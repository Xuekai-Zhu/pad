def solution():
    """A charity is delivering chicken and rice dinners to a shelter for the hungry. They have a hundred plates to deliver. The rice cost ten cents a plate and the chicken cost forty cents a plate. How many dollars did the charity spend on the food for the dinners?"""
    # Define the cost of rice and chicken per plate
    RICE_COST = 0.1
    CHICKEN_COST = 0.4

    # Define the number of plates to deliver
    NUM_PLATES = 100

    # Calculate the total cost of rice and chicken
    total_cost = (RICE_COST + CHICKEN_COST) * NUM_PLATES

    # return the result
    result = round(total_cost, 2)
    return result

print(solution())