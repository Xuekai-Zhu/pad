def solution():
    """Two puppies, two kittens, and three parakeets were for sale at the pet shop. The puppies were three times more expensive than the parakeets, and the parakeets were half as expensive as the kittens. If the cost of one parakeet was $10, what would it cost to purchase all of the pets for sale at the pet shop, in dollars?"""
    parakeet_cost = 10
    kitten_cost = 2 * parakeet_cost
    puppy_cost = 3 * parakeet_cost
    total_cost = (2 * puppy_cost) + (2 * kitten_cost) + (3 * parakeet_cost)
    result = total_cost
    return result

print(solution())