def solution():
    cool_cats = 5  # Cat Cafe Cool has 5 cats
    paw_cats = 2 * cool_cats  # Cat Cafe Paw has 2 times as many cats as Cat Cafe Cool
    meow_cats = 3 * paw_cats  # Cat Cafe Meow has 3 times as many cats as Cat Cafe Paw

    # Calculate the total number of cats in Cat Cafe Meow and Cat Cafe Paw
    total_cats = paw_cats + meow_cats
    result = total_cats
    return result

print(solution())