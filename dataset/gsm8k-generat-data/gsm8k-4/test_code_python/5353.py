def solution():
    """A pet shop has 2 puppies and some kittens. A puppy costs $20, and a kitten costs $15. If the stock is worth $100, how many kittens does the pet shop have?"""
    # Define the cost of a puppy and a kitten
    puppy_cost = 20
    kitten_cost = 15

    # Define the number of puppies
    num_puppies = 2

    # Calculate the total value of the stock
    total_value = num_puppies * puppy_cost + x * kitten_cost

    # Solve for the number of kittens
    x = (100 - num_puppies * puppy_cost) / kitten_cost

    # Round the number of kittens to the nearest whole number
    num_kittens = round(x)

    # Return the result
    result = num_kittens
    return result

print(solution())