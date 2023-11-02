def solution():
    # Calculate the total cost to get the cats ready for adoption
    cat_cost = 50 * 2  # Two cats are adopted, and it costs $50 each to get them ready

    # Calculate the total cost to get the adult dogs ready for adoption
    adult_dog_cost = 100 * 3  # Three adult dogs are adopted, and it costs $100 each to get them ready

    # Calculate the total cost to get the puppies ready for adoption
    puppy_cost = 150 * 2  # Two puppies are adopted, and it costs $150 each to get them ready

    # Calculate the total cost to get all the animals ready for adoption
    total_cost = cat_cost + adult_dog_cost + puppy_cost
    result = total_cost
    return result

print(solution())