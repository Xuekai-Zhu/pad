def solution():
    
    eggs_per_basket = 9
    eggs_per_flan = 3
    flans_to_make = 15
    eggs_needed = eggs_per_flan * flans_to_make
    babysitting_eggs = eggs_needed // eggs_per_basket
    result = babysitting_eggs
    return result

print(solution())