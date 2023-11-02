def solution():
    # Calculate the number of hens
    total_roosters = 39
    total_chickens = 440
    total_hens = total_chickens - total_roosters
    non_laying_hens = 15
    laying_hens = total_hens - non_laying_hens
    
    # Calculate the total number of eggs
    eggs_per_laying_hen = 3
    total_eggs = laying_hens * eggs_per_laying_hen
    
    result = total_eggs
    return result

print(solution())