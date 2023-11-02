def solution():
    # Calculate the total amount of soup
    milk = 2
    veg_stock = 3 * 1
    total_soup = milk + veg_stock

    # Calculate the number of bags needed
    bag_size = 3
    bags_needed = total_soup / bag_size

    # Round up the number of bags to ensure enough space for all the soup
    bags_needed = math.ceil(bags_needed)

    result = bags_needed
    return result

print(solution())