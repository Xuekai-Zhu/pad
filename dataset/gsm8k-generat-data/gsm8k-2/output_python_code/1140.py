def solution():
    """A pet store owner had 12 birds, 9 puppies, 5 cats, and 15 spiders. Half the birds were sold and 3 puppies were adopted. Then, someone left the spider enclosure open and 7 of them went loose. How many animals does the pet store owner have left?"""
    birds = 12
    puppies = 9 - 3
    cats = 5
    spiders = 15 - 7
    birds_sold = birds // 2
    total_animals = birds_sold + puppies + cats + spiders
    result = total_animals
    return result

print(solution())