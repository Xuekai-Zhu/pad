def solution():
    """Carmen had 28 cats and 18 dogs before she gave 3 of the cats up for adoption. How many more cats than dogs does Carmen have now?"""
    # Define the initial number of cats and dogs
    initial_cats = 28
    initial_dogs = 18

    # Subtract the number of cats given up for adoption
    final_cats = initial_cats - 3

    # Calculate the difference between the final number of cats and dogs
    cat_dog_difference = final_cats - initial_dogs

    result = cat_dog_difference
    return result

print(solution())