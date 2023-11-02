def solution():
    """A chef needs to make french fries. He can get 25 fries out of 1 potato. He has 15 potatoes and he needs 200 fries. How many potatoes will he have leftover?"""
    fries_per_potato = 25
    total_fries_needed = 200
    potatoes_available = 15
    total_fries_available = fries_per_potato * potatoes_available
    leftover_potatoes = potatoes_available - ((total_fries_available - total_fries_needed) // fries_per_potato)
    result = leftover_potatoes
    return result

print(solution())