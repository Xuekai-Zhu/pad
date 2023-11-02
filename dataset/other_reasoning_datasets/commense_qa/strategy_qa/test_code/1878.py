def solution():
    mollusk_animals = ["snails", "slugs", "mussels", "octopuses"]
    chinese_animals = ["rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "goat", "monkey", "rooster", "dog", "pig"]
    overlap = [animal for animal in mollusk_animals if animal in chinese_animals]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())