def solution():
    # Calculate the total number of legs of the animals for sale
    legs_birds = 2 * 3  # Each bird has two legs
    legs_dogs = 4 * 5  # Each dog has four legs
    legs_snakes = 0  # Snakes are legless
    legs_spiders = 8  # Spiders have eight legs
    total_legs = legs_birds + legs_dogs + legs_snakes + legs_spiders

    result = total_legs
    return result

print(solution())