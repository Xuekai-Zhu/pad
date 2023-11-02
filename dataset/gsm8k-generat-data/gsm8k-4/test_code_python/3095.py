def solution():
    """In a Zoo, there are different animals. There are 5 giraffes and twice as many penguins. Penguins make up 20% of all the animals in the Zoo. How many elephants are there in the Zoo if they make up 4% of all the animals?"""
    # Calculate the total number of penguins in the zoo
    total_penguins = 5 * 2 / 0.2

    # Calculate the total number of animals in the zoo
    total_animals = total_penguins / 0.2

    # Calculate the number of elephants in the zoo
    elephants = total_animals * 0.04

    result = elephants
    return result

print(solution())