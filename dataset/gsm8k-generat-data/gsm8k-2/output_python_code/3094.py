def solution():
    """In a Zoo, there are different animals. There are 5 giraffes and twice as many penguins. Penguins make up 20% of all the animals in the Zoo. How many elephants are there in the Zoo if they make up 4% of all the animals?"""
    giraffes = 5
    penguins = giraffes * 2
    total_animals = (penguins / 0.2)
    elephants = total_animals * 0.04
    result = elephants
    return result

print(solution())