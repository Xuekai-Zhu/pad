def solution():
    """Antonov bought 60 candies. He gave a pack of candy to his sister. If a pack of candy has 20 pieces, how many packs does Antonov still have?"""
    # Define the initial number of candies
    initial_candies = 60

    # Subtract the candies Antonov gave to his sister
    remaining_candies = initial_candies - 20

    # Calculate the number of packs of candies Antonov still has
    packs_of_candies = remaining_candies // 20

    # Return the result
    result = packs_of_candies
    return result

print(solution())