def solution():
    """A chef needs to make french fries. He can get 25 fries out of 1 potato. He has 15 potatoes and he needs 200 fries. How many potatoes will he have leftover?"""
    fries_per_potato = 25
    potatoes_available = 15
    fries_needed = 200
    total_fries = fries_per_potato * potatoes_available
    potatoes_used = fries_needed // fries_per_potato
    potatoes_leftover = potatoes_available - potatoes_used
    result = potatoes_leftover
    return result

print(solution())