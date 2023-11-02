def solution():
    # Calculate the number of tigers in the zoo
    num_tigers = 4 * 4  # 4 tiger enclosures each with 4 tigers

    # Calculate the number of zebras in the zoo
    num_zebras = 2 * 4 * 10  # 4 tiger enclosures each with 2 zebra enclosures each with 10 zebras

    # Calculate the number of giraffes in the zoo
    num_giraffes = 3 * num_zebras * 2  # 3 times as many giraffe enclosures as zebra enclosures, each giraffe enclosure has 2 giraffes

    # Calculate the total number of animals in the zoo
    total_animals = num_tigers + num_zebras + num_giraffes
    result = total_animals
    return result

print(solution())