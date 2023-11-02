def solution():
    hens = 10
    eggs_laid = 80
    days = 10
    new_hens = 15
    new_days = 15
    new_eggs_laid = ((hens + new_hens) / days) * new_days
    result = new_eggs_laid
    return result

print(solution())