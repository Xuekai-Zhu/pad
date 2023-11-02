def solution():
    # Starting numbers of animals
    birds = 12
    puppies = 9
    cats = 5
    spiders = 15

    # Calculate the numbers of animals that are sold or adopted
    sold_birds = birds // 2
    adopted_puppies = 3

    # Calculate the numbers of animals that escape or are left
    escaped_spiders = 7

    # Calculate the remaining numbers of animals
    remaining_birds = birds - sold_birds
    remaining_puppies = puppies - adopted_puppies
    remaining_cats = cats
    remaining_spiders = spiders - escaped_spiders

    # Calculate the total number of remaining animals
    remaining_animals = remaining_birds + remaining_puppies + remaining_cats + remaining_spiders
    result = remaining_animals
    return result

print(solution())