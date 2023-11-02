def solution():
    dogs = 6  # The pet store has 6 dogs for sale
    cats = dogs / 2  # The number of cats is half the number of dogs
    birds = dogs * 2  # The number of birds is twice the number of dogs
    fish = dogs * 3  # The number of fish is thrice the number of dogs

    # Calculate the total number of animals for sale
    total_animals = dogs + cats + birds + fish
    result = total_animals
    return result

print(solution())