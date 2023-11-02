def solution():
    """There are twice as many centipedes as humans on a certain island and half as many sheep as humans. How many sheep and humans in total are on the island if the number of centipedes is 100?"""
    # Define the number of centipedes
    centipedes = 100

    # Calculate the number of humans
    humans = centipedes // 2

    # Calculate the number of sheep
    sheep = humans // 2

    # Calculate the total number of animals on the island
    total_animals = centipedes + humans + sheep

    # Display the total number of animals on the island
    result = total_animals
    return result

print(solution())