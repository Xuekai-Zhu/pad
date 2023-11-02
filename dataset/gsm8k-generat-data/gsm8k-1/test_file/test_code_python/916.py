def solution():
    """Larry loves taking care of animals. He has 3 cats. He has 3 times as many dogs as cats. He has 2 fewer rabbits than dogs. He has a fish tank with three times the number of fish as rabbits. He also has a collection of gerbils that's 1/3 the number of fish he has. How many pets does Larry have?"""
    cats = 3
    dogs = cats * 3
    rabbits = dogs - 2
    fish = rabbits * 3
    gerbils = fish / 3
    total_pets = cats + dogs + rabbits + fish + gerbils
    result = total_pets
    return result

print(solution())