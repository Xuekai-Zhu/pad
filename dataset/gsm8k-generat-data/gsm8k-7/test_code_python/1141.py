def solution():
    num_birds = 12
    num_puppies = 9
    num_cats = 5
    num_spiders = 15

    # Calculate the number of birds remaining after selling half
    num_birds_remaining = num_birds / 2

    # Calculate the number of puppies remaining after adoption
    num_puppies_remaining = num_puppies - 3

    # Calculate the number of spiders remaining after 7 escaped
    num_spiders_remaining = num_spiders - 7

    # Calculate the total number of animals remaining
    num_animals_remaining = num_birds_remaining + num_puppies_remaining + num_cats + num_spiders_remaining
    result = num_animals_remaining
    return result

print(solution())