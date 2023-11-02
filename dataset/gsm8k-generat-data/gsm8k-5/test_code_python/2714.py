def solution():
    cost_parakeet = 10  # Cost of one parakeet is $10
    cost_kitten = 2 * cost_parakeet  # Parakeets are half as expensive as kittens
    cost_puppy = 3 * cost_parakeet  # Puppies are three times more expensive than parakeets

    # Calculate the total cost of all pets
    total_cost = 2 * cost_puppy + 2 * cost_kitten + 3 * cost_parakeet
    result = total_cost
    return result

print(solution())