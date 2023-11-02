def solution():
    """Carmen had 28 cats and 18 dogs before she gave 3 of the cats up for adoption. How many more cats than dogs does Carmen have now?"""
    initial_cats = 28
    initial_dogs = 18
    cats_adopted = 3
    remaining_cats = initial_cats - cats_adopted
    difference = remaining_cats - initial_dogs
    result = difference
    return result

print(solution())