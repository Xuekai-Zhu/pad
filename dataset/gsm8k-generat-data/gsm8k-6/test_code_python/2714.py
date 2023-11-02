def solution():
    # Calculate the cost of one kitten
    cost_parakeet = 10  # cost of one parakeet
    cost_kitten = 2 * cost_parakeet  # parakeets are half as expensive as kittens

    # Calculate the cost of one puppy
    cost_puppy = 3 * cost_parakeet  # puppies are three times more expensive than parakeets

    # Calculate the total cost of all the pets
    total_cost = 2 * cost_puppy + 2 * cost_kitten + 3 * cost_parakeet
    result = total_cost
    return result

print(solution())