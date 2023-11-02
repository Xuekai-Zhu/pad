def solution():
    """Two puppies, two kittens, and three parakeets were for sale at the pet shop. The puppies were three times more expensive than the parakeets, and the parakeets were half as expensive as the kittens. If the cost of one parakeet was $10, what would it cost to purchase all of the pets for sale at the pet shop, in dollars?"""
    num_puppies = 2
    num_kittens = 2
    num_parakeets = 3
    cost_parakeet = 10
    cost_kitten = cost_parakeet * 2
    cost_puppy = cost_parakeet * 2 * 3
    total_cost = (num_puppies * cost_puppy) + (num_kittens * cost_kitten) + (num_parakeets * cost_parakeet)
    result = total_cost
    return result

print(solution())