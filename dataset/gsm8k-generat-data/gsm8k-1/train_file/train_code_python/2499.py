def solution():
    """Claire wants to make 2 cakes for her mother. Two packages of flour are required for making a cake. If 1 package of flour is $3, how much does she pay for the flour that is enough to make 2 cakes?"""
    packages_per_cake = 2
    cakes = 2
    price_per_package = 3
    total_packages = packages_per_cake * cakes
    total_price = total_packages * price_per_package
    result = total_price
    return result

print(solution())