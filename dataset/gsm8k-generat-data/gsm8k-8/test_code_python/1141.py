def solution():
    # Calculate the new numbers of each animal after selling/adopting/losing some
    num_birds = 12 // 2  # Using integer division to get the new number of birds
    num_puppies = 9 - 3
    num_cats = 5
    num_spiders = 15 - 7

    # Calculate the total number of animals left
    total_animals_left = num_birds + num_puppies + num_cats + num_spiders
    result = total_animals_left
    return result

print(solution())