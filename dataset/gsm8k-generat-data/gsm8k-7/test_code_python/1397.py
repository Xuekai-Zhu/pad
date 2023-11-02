def solution():
    milk = 2  # in quarts
    veg_stock = 3  # in quarts
    veg_puree = 1  # in quarts
    total_soup = milk + (veg_stock * veg_puree)
    bags = total_soup / 3  # in quarts
    result = bags
    return result

print(solution())