def solution():
    """Mary is trying to count the animals in the petting zoo, but they kept moving around so she double-counts 7 sheep and forgets to count 3 pigs. If Mary thinks there are 60 animals, how many are there really?"""
    # Define the number of double-counted sheep and uncounted pigs
    double_sheep = 7
    uncounted_pigs = 3

    # Calculate the number of actual sheep and pigs
    sheep = (60 - double_sheep + uncounted_pigs) / 2
    pigs = sheep - uncounted_pigs

    # Calculate the total number of animals
    total_animals = sheep + pigs

    # Display the total number of animals
    result = total_animals
    return result

print(solution())