def solution():
    """A pet shop has 2 puppies and some kittens. A puppy costs $20, and a kitten costs $15. If the stock is worth $100, how many kittens does the pet shop have?"""
    num_puppies = 2
    puppy_price = 20
    kitten_price = 15
    total_price = 100
    total_puppy_price = num_puppies * puppy_price
    total_kitten_price = total_price - total_puppy_price
    num_kittens = total_kitten_price // kitten_price
    result = num_kittens
    return result

print(solution())