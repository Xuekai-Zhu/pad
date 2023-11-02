def solution():
    """A pet shop has 2 puppies and some kittens. A puppy costs $20, and a kitten costs $15. If the stock is worth $100, how many kittens does the pet shop have?"""
    # Define the cost of a puppy and a kitten
    PUPPY_COST = 20
    KITTEN_COST = 15

    # Define the number of puppies in stock
    num_puppies = 2

    # Calculate the amount of money spent on puppies
    puppy_cost = num_puppies * PUPPY_COST

    # Calculate the amount of money left for kittens
    kitten_money = 100 - puppy_cost

    # Calculate the number of kittens
    num_kittens = kitten_money // KITTEN_COST

    # Display the number of kittens
    result = num_kittens
    return result

print(solution())