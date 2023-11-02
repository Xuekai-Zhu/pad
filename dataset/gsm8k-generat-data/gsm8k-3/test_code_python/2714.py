def solution():
    """Two puppies, two kittens, and three parakeets were for sale at the pet shop.  The puppies were three times more expensive than the parakeets, and the parakeets were half as expensive as the kittens.  If the cost of one parakeet was $10, what would it cost to purchase all of the pets for sale at the pet shop, in dollars?"""
    # Define the cost of one parakeet and the relationships between costs of different pets
    PARAKEET_COST = 10
    KITTEN_COST = 2 * PARAKEET_COST
    PUPPY_COST = 3 * PARAKEET_COST

    # Calculate the total cost of all the pets
    total_cost = 2 * PUPPY_COST + 2 * KITTEN_COST + 3 * PARAKEET_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())