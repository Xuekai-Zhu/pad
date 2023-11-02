def solution():
    """Jezebel needs to buy two dozens of red roses and 3 pieces of sunflowers for a bouquet that she is going to arrange. Each red rose costs $1.50 and each sunflower costs $3. How much will Jezebel pay for all those flowers?"""
    # Define the number of flowers to be bought
    roses = 24   # Two dozens
    sunflowers = 3

    # Define the cost of each type of flower
    rose_cost = 1.5
    sunflower_cost = 3

    # Calculate the total cost of all the flowers
    total_cost = (roses * rose_cost) + (sunflowers * sunflower_cost)

    # Return the result
    result = total_cost
    return result

print(solution())