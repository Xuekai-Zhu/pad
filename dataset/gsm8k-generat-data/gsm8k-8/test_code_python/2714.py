def solution():
    # Define the cost of one parakeet and calculate the cost of one kitten and one puppy
    parakeet_cost = 10
    kitten_cost = 2 * parakeet_cost
    puppy_cost = 3 * parakeet_cost

    # Calculate the total cost of all pets
    total_cost = 2 * puppy_cost + 2 * kitten_cost + 3 * parakeet_cost
    result = total_cost
    return result

print(solution())