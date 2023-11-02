def solution():
    initial_birds = 12
    initial_puppies = 9
    initial_cats = 5
    initial_spiders = 15
    sold_birds = initial_birds / 2
    adopted_puppies = 3
    remaining_birds = initial_birds - sold_birds
    escaped_spiders = 7
    remaining_spiders = initial_spiders - escaped_spiders
    total_remaining = remaining_birds + initial_puppies + initial_cats + remaining_spiders
    result = total_remaining
    return result

print(solution())