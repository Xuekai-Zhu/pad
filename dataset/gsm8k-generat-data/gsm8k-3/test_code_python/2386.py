def solution():
    """An animal shelter recently took in twelve cats. The shelter already had half that number of cats. Two days later, three had been adopted. The next day, one of the cats had five kittens, and one person arrived to pick up one of the cats that was their missing pet. How many cats does the shelter have now?"""
    # Define the number of cats the shelter had before taking in 12 cats
    initial_cats = 6

    # Calculate the number of cats that remained after three were adopted
    remaining_cats = initial_cats + 12 - 3

    # Calculate the number of cats after one had five kittens
    cats_with_kittens = remaining_cats + 5

    # Calculate the final number of cats after one was picked up by their owner
    final_cats = cats_with_kittens - 1

    # Display the final number of cats at the shelter
    result = final_cats
    return result

print(solution())