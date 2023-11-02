def solution():
    """An animal shelter recently took in twelve cats. The shelter already had half that number of cats. Two days later, three had been adopted. The next day, one of the cats had five kittens, and one person arrived to pick up one of the cats that was their missing pet. How many cats does the shelter have now?"""
    # Define the initial number of cats
    initial_cats = 6

    # Define the number of cats taken in
    taken_in_cats = 12

    # Calculate the total number of cats now
    total_cats = initial_cats + taken_in_cats - 3 + 5 - 1

    # return the result
    result = total_cats
    return result

print(solution())