def solution():
    """Jezebel needs to buy two dozens of red roses and 3 pieces of sunflowers for a bouquet that she is going to arrange. Each red rose costs $1.50 and each sunflower costs $3. How much will Jezebel pay for all those flowers?"""
    # Define the cost of each type of flower
    ROSE_PRICE = 1.5
    SUNFLOWER_PRICE = 3

    # Define the number of flowers Jezebel needs to buy
    num_roses = 24
    num_sunflowers = 3

    # Calculate the total cost of the red roses
    rose_cost = num_roses * ROSE_PRICE

    # Calculate the total cost of the sunflowers
    sunflower_cost = num_sunflowers * SUNFLOWER_PRICE

    # Calculate the total cost of all the flowers
    total_cost = rose_cost + sunflower_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())