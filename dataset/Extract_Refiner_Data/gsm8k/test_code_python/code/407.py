def solution():
    
    # Define the cost of each package of fireworks
    PACKAGE_COST = 400

    # Define the cost of each pack of fireworks
    PACK_COST = 2 * PACKAGE_COST

    # Calculate the total cost of the package of fireworks
    package_cost = PACKAGE_COST + PACK_COST

    # Calculate the discounted cost of the package of fireworks
    discounted_cost = package_cost * 0.8

    # Calculate the total cost of the finale firework
    finale_cost = 150

    # Calculate the total cost of all the fireworks
    total_cost = discounted_cost + finale_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())