def solution():
    # Define the number of guppies Rick bought
    rick_guppies = 30

    # Calculate the number of clowns Tim bought
    tim_clowns = 2 * rick_guppies

    # Calculate the number of tetras you bought
    your_tetras = 4 * tim_clowns

    # Calculate the total number of animals bought
    total_animals = rick_guppies + tim_clowns + your_tetras
    result = total_animals
    return result

print(solution())