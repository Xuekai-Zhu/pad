def solution():
    
    total_eggs = 60
    eggs_in_fridge = 10
    eggs_for_cakes = total_eggs - eggs_in_fridge
    eggs_per_cake = 5
    cakes = eggs_for_cakes // eggs_per_cake
    result = cakes
    return result

print(solution())