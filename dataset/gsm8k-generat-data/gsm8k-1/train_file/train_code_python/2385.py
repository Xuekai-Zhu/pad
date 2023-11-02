def solution():
    """An animal shelter recently took in twelve cats. The shelter already had half that number of cats. Two days later, three had been adopted. The next day, one of the cats had five kittens, and one person arrived to pick up one of the cats that was their missing pet. How many cats does the shelter have now?"""
    initial_cats = 6
    new_cats = 12
    adopted_cats = 3
    kitten_cats = 5
    missing_cats = 1
    total_cats = initial_cats + new_cats - adopted_cats + kitten_cats - missing_cats
    result = total_cats
    return result

print(solution())