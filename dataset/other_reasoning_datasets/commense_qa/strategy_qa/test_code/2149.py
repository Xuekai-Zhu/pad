def solution():
    pyramid_workers = 30000
    roman_gallic_army = 75000
    if roman_gallic_army < pyramid_workers:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())