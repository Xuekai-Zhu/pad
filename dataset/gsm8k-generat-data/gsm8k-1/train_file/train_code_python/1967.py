def solution():
    """Cat Cafe Meow has 3 times as many cats as Cat Cafe Paw. Cat Cafe Paw has 2 times as many cats as Cat Cafe Cool. If Cat Cafe Cool has 5 cats, how many cats are there in Cat Cafe Meow and Cat Cafe Paw?"""
    cool_cats = 5
    paw_cats = cool_cats * 2
    meow_cats = paw_cats * 3
    total_cats = paw_cats + meow_cats
    result = total_cats
    return result

print(solution())