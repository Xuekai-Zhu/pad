def solution():
    
    eggs_ordered = 3 * 12
    eggs_for_crepes = eggs_ordered / 4
    eggs_remaining = eggs_ordered - eggs_for_crepes
    eggs_for_cupcakes = eggs_remaining * (2 / 3)
    eggs_for_breakfast = eggs_remaining - eggs_for_cupcakes
    result = eggs_for_breakfast
    return result

print(solution())