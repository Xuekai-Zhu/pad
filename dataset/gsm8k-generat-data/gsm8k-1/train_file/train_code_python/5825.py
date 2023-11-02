def solution():
    """A dog runs through a field and is joined by a group of 4 cats. 2 rabbits join each cat and 3 hares join each rabbit. How many animals are running through the field?"""
    cats = 4
    rabbits_per_cat = 2
    hares_per_rabbit = 3
    total_animals = 1 + (cats + (cats * rabbits_per_cat) + (cats * rabbits_per_cat * hares_per_rabbit))
    result = total_animals
    return result

print(solution())