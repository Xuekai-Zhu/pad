def solution():
    """Two puppies, two kittens, and three parakeets were for sale at the pet shop. The puppies were three times more expensive than the parakeets, and the parakeets were half as expensive as the kittens. If the cost of one parakeet was $10, what would it cost to purchase all of the pets for sale at the pet shop, in dollars?"""
    # Define the price of one parakeet
    parakeet_price = 10

    # Calculate the price of one kitten
    kitten_price = parakeet_price * 2

    # Calculate the price of one puppy
    puppy_price = parakeet_price * 6

    # Calculate the total cost of all the pets
    total_cost = (2 * puppy_price) + (2 * kitten_price) + (3 * parakeet_price)

    # return the result
    result = total_cost
    return result

print(solution())