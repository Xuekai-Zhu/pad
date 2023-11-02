def solution():
    """Cat Cafe Meow has 3 times as many cats as Cat Cafe Paw. Cat Cafe Paw has 2 times as many cats as Cat Cafe Cool. If Cat Cafe Cool has 5 cats, how many cats are there in Cat Cafe Meow and Cat Cafe Paw?"""
    # Define the number of cats in Cat Cafe Cool
    cool_cats = 5

    # Calculate the number of cats in Cat Cafe Paw
    paw_cats = 2 * cool_cats

    # Calculate the number of cats in Cat Cafe Meow
    meow_cats = 3 * paw_cats

    # Calculate the total number of cats
    total_cats = paw_cats + meow_cats

    # Display the total number of cats
    result = total_cats
    return result

print(solution())