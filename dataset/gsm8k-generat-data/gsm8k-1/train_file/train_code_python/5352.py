def solution():
    """A pet shop has 2 puppies and some kittens. A puppy costs $20, and a kitten costs $15. If the stock is worth $100, how many kittens does the pet shop have?"""
    num_puppies = 2
    puppy_cost = 20
    kitten_cost = 15
    total_cost = 100
    remaining_cost = total_cost - (num_puppies * puppy_cost)
    num_kittens = remaining_cost / kitten_cost
    result = num_kittens
    return result

print(solution())