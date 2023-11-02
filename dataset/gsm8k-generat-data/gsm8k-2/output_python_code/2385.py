def solution():
    """An animal shelter recently took in twelve cats. The shelter already had half that number of cats. Two days later, three had been adopted. The next day, one of the cats had five kittens, and one person arrived to pick up one of the cats that was their missing pet. How many cats does the shelter have now?"""
    initial_cats = 6
    current_cats = initial_cats + 12 - 3 - 1 + 5 - 1
    result = current_cats
    return result

print(solution())