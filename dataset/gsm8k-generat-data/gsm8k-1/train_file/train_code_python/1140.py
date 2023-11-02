def solution():
    """A pet store owner had 12 birds, 9 puppies, 5 cats, and 15 spiders. Half the birds were sold and 3 puppies were adopted. Then, someone left the spider enclosure open and 7 of them went loose. How many animals does the pet store owner have left?"""
    initial_birds = 12
    initial_puppies = 9
    initial_cats = 5
    initial_spiders = 15
    sold_birds = initial_birds // 2
    adopted_puppies = 3
    escaped_spiders = 7
    remaining_birds = initial_birds - sold_birds
    remaining_puppies = initial_puppies - adopted_puppies
    remaining_cats = initial_cats
    remaining_spiders = initial_spiders - escaped_spiders
    total_remaining_animals = remaining_birds + remaining_puppies + remaining_cats + remaining_spiders
    result = total_remaining_animals
    
    return result

print(solution())