def solution():
    """In a Zoo, there are different animals. There are 5 giraffes and twice as many penguins. Penguins make up 20% of all the animals in the Zoo. How many elephants are there in the Zoo if they make up 4% of all the animals?"""
    giraffes = 5
    penguins = giraffes * 2
    penguins_percentage = 20
    total_animals = (penguins / (penguins_percentage / 100))
    elephants_percentage = 4
    elephants = total_animals * (elephants_percentage / 100)
    result = elephants
    return result

print(solution())