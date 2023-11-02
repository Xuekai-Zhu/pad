def solution():
    """Martin owns a farm with hens. 10 hens do lay 80 eggs in 10 days. Martin decided to buy 15 more hens. How many eggs will all hens lay in 15 days?"""
    initial_hens = 10
    initial_eggs = 80
    initial_days = 10
    additional_hens = 15
    additional_days = 15
    eggs_per_hen = initial_eggs / initial_hens
    total_hens = initial_hens + additional_hens
    eggs_increased = eggs_per_hen * additional_hens * additional_days
    total_eggs = (initial_eggs * additional_days) + eggs_increased
    result = total_eggs
    return result

print(solution())