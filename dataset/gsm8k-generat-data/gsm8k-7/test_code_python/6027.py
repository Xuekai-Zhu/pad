def solution():
    num_eggs = 10
    eggs_used_for_omelet = 5
    num_chickens = 2
    eggs_laid_per_chicken = 3

    # Calculate how many eggs were laid by the chickens
    eggs_laid = num_chickens * eggs_laid_per_chicken

    # Calculate how many eggs the family has now
    total_eggs = num_eggs - eggs_used_for_omelet + eggs_laid
    result = total_eggs
    return result

print(solution())