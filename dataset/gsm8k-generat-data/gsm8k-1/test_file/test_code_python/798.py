def solution():
    """Bubbles collects stuffed animals. She has three stuffed puppies, five stuffed koalas, two stuffed zebras and four stuffed frogs. If she wants to buy enough stuffed goats, such that the percentage of stuffed goats is 30% of all of her stuffed animals, how many stuffed goats should she buy?"""
    total_animals = 3 + 5 + 2 + 4
    percentage_goats = 0.3
    current_goats = 0
    needed_goats = int((total_animals * percentage_goats - current_goats) / (1 - percentage_goats))
    result = needed_goats
    return result

print(solution())