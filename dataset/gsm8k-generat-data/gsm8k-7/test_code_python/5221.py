def solution():
    num_eggs = 60
    eggs_in_fridge = 10
    eggs_for_cakes = num_eggs - eggs_in_fridge
    eggs_per_cake = 5
    num_cakes = eggs_for_cakes // eggs_per_cake
    result = num_cakes
    return result

print(solution())