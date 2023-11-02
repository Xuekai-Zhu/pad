def solution():
    katy_flour = 3 * 5
    wendi_flour = 2 * katy_flour
    carrie_flour = wendi_flour - 5
    carrie_flour_ounces = carrie_flour * 16
    katy_flour_ounces = katy_flour * 16
    difference = carrie_flour_ounces - katy_flour_ounces
    result = difference
    return result

print(solution())