def solution():
    num_giraffes = 5
    penguins_ratio = 2
    penguins_percent = 20
    elephants_percent = 4

    # Calculate the total number of penguins in the zoo
    total_animals_percent = 100
    penguins_percent_of_total = penguins_percent / total_animals_percent
    total_penguins = int(penguins_percent_of_total * (num_giraffes + (num_giraffes*penguins_ratio)))

    # Calculate the total number of animals in the zoo
    total_animals = num_giraffes + total_penguins

    # Calculate the number of elephants in the zoo
    elephants_percent_of_total = elephants_percent / total_animals_percent
    num_elephants = int(elephants_percent_of_total * total_animals)

    result = num_elephants
    return result

print(solution())