def solution():
    # Calculate the number of zebra and giraffe enclosures
    num_zebra_enclosures = 4 * 2
    num_giraffe_enclosures = 3 * num_zebra_enclosures

    # Calculate the number of tigers, zebras, and giraffes in the zoo
    num_tigers = 4 * 4
    num_zebras = num_zebra_enclosures * 10
    num_giraffes = num_giraffe_enclosures * 2

    # Calculate the total number of animals in the zoo
    total_animals = num_tigers + num_zebras + num_giraffes
    result = total_animals
    return result

print(solution())