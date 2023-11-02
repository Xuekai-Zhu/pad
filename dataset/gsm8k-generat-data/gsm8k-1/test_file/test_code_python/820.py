def solution():
    """
    Kimberly bought 8 packages of cat food and 6 packages of dog food. Each package of cat food contained 11 tins,
    and each package of dog food contained 6 tins. How many more tins of cat food than dog food did Kimberly buy?
    """
    cat_packages = 8
    dog_packages = 6
    tins_per_cat_package = 11
    tins_per_dog_package = 6
    total_cat_tins = cat_packages * tins_per_cat_package
    total_dog_tins = dog_packages * tins_per_dog_package
    difference = total_cat_tins - total_dog_tins
    result = difference
    return result

print(solution())