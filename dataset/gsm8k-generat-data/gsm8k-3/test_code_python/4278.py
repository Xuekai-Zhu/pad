def solution():
    """Antonov bought 60 candies. He gave a pack of candy to his sister. If a pack of candy has 20 pieces, how many packs does Antonov still have?"""
    # Calculate the number of packs Antonov had initially
    initial_packs = 60/20

    # Subtract one pack for the candy given to his sister
    remaining_packs = initial_packs - 1

    # Display the remaining number of packs
    result = remaining_packs
    return result

print(solution())