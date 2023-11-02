def solution():
    num_tiger_enclosures = 4
    num_zebra_enclosures = num_tiger_enclosures * 2
    num_giraffe_enclosures = num_zebra_enclosures * 3

    num_tigers_per_enclosure = 4
    num_zebras_per_enclosure = 10
    num_giraffes_per_enclosure = 2

    # Calculate the total number of tigers in the zoo
    total_tigers = num_tiger_enclosures * num_tigers_per_enclosure

    # Calculate the total number of zebras in the zoo
    total_zebras = num_zebra_enclosures * num_zebras_per_enclosure

    # Calculate the total number of giraffes in the zoo
    total_giraffes = num_giraffe_enclosures * num_giraffes_per_enclosure

    # Calculate the total number of animals in the zoo
    total_animals = total_tigers + total_zebras + total_giraffes
    result = total_animals
    return result

print(solution())