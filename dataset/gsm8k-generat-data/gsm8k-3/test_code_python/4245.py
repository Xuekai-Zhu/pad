def solution():
    """In a day, Sam hunts 6 animals. Rob hunts half as many animals as Sam. Mark hunts 1/3 of the total of what Rob and Sam hunt. If Peter hunts 3 times as many animals as Mark does, how many animals do they all hunt in a day?"""
    # Define the number of animals hunted by Sam
    sam_animals = 6

    # Define the number of animals hunted by Rob (half as many as Sam)
    rob_animals = sam_animals / 2

    # Define the total number of animals hunted by Rob and Sam
    rob_sam_animals = rob_animals + sam_animals

    # Define the number of animals hunted by Mark (1/3 of the total of what Rob and Sam hunt)
    mark_animals = (1/3) * rob_sam_animals

    # Define the number of animals hunted by Peter (3 times as many as Mark)
    peter_animals = 3 * mark_animals

    # Calculate the total number of animals hunted
    total_animals = sam_animals + rob_animals + mark_animals + peter_animals

    # Display the total number of animals hunted
    result = total_animals
    return result

print(solution())